from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from users.views import UserRegisterView, ProfileView, LoginLogListView

urlpatterns = [
    path('users/register/', UserRegisterView.as_view(), name='register'),
    path('auth/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('users/me/', ProfileView.as_view(), name='profile'),
    path('logs/login/', LoginLogListView.as_view(), name='login_logs'),
]
