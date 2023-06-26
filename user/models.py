from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    username = models.CharField(max_length=40)
    email = models.EmailField(unique=True, max_length=255)
    name = models.CharField(max_length=50, null=True, blank=True)
    password = models.CharField(max_length=50)
    registerd_date = models.DateField(auto_now_add=True)
    
    # 아이디로 지정
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
    def __str__(self):
        return self.name