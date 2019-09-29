from django.db import models
from django.utils import timezone

# Create your models here.

class Login(models.Model):
    username = models.CharField(max_length=255, verbose_name='Username', unique=True)
    senha = models.CharField(max_length=16, verbose_name='Senha')
