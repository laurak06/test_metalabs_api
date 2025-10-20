from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from users.views import UserRegisterView, ProfileView, LoginLogListView, ActivateView,\
    ForgotPasswordView, RestorePasswordView, CustomTokenObtainPairView

urlpatterns = [
    path('users/register/', UserRegisterView.as_view(), name='register'),
    path('auth/token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('users/me/', ProfileView.as_view(), name='profile'),
    path('logs/login/', LoginLogListView.as_view(), name='login_logs'),
    path('users/activate/', ActivateView.as_view()),
    path('users/forgot/', ForgotPasswordView.as_view()),
    path('users/restore/', RestorePasswordView.as_view()),
]
