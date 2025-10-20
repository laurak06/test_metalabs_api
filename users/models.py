import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models

from .manager import UserManager

class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    is_active = models.BooleanField(default=False)
    activation_code = models.CharField(max_length=300, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def create_activation_code(self):
        self.activation_code = str(uuid.uuid4())
        self.save()

    def __str__(self):
        return f'{self.email}'

class LoginLog(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='login_logs')
    timestamp = models.DateTimeField(auto_now_add=True)
    ip_address = models.GenericIPAddressField()
    user_agent = models.CharField(max_length=256)

    def __str__(self):
        return f"{self.user.username} - {self.timestamp}"
