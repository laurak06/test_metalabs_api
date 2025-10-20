from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, permissions
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework_simplejwt.views import TokenObtainPairView
from django.shortcuts import get_object_or_404

from .models import LoginLog
from .serializers import UserRegisterSerializer, LoginLogSerializer, ForgotPasswordSerializer,\
    RestorePasswordSerializer, UserSerializer, CustomTokenObtainPairSerializer
from .send_email import send_reset_password
from .models import CustomUser

class UserRegisterView(generics.CreateAPIView):
    serializer_class = UserRegisterSerializer


class ActivateView(APIView):
    def get(self, request):
        activation_code = request.query_params.get('code')
        user = get_object_or_404(CustomUser, activation_code=activation_code)
        user.is_active = True
        user.activation_code = ''
        user.save()
        return Response({'message': 'Вы успешно подтвердили почту'})


class ForgotPasswordView(APIView):
    def post(self, request):
        serializer = ForgotPasswordSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            user = CustomUser.objects.get(email=serializer.data.get('email'))
            user.create_activation_code()
            user.save()
            send_reset_password(user)
            return Response({'message': 'Проверьте почту'})
        except CustomUser.DoesNotExist:
            return Response({'error': 'Пользователь с таким email не найден'}, status=404)


class RestorePasswordView(APIView):
    def post(self, request):
        serializer = RestorePasswordSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'message': 'Пароль успешно поменялся'})


class ProfileView(generics.RetrieveUpdateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        if response.status_code == 200:
            user = self.get_serializer().validated_data['user']
            ip = request.META.get('REMOTE_ADDR')
            ua = request.META.get('HTTP_USER_AGENT', '')
            LoginLog.objects.create(user=user, ip_address=ip, user_agent=ua)
        return response

class LoginLogListView(generics.ListAPIView):
    queryset = LoginLog.objects.all()
    serializer_class = LoginLogSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['user__id']

    def get_queryset(self):
        queryset = super().get_queryset()
        start_date = self.request.query_params.get('start_date')
        end_date = self.request.query_params.get('end_date')
        if start_date:
            queryset = queryset.filter(timestamp__gte=start_date)
        if end_date:
            queryset = queryset.filter(timestamp__lte=end_date)
        return queryset