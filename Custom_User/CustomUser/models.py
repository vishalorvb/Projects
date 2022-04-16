from django.db import models
from django.contrib.auth.models import AbstractUser
from django.forms import CharField
from .manager import *



class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=12 , unique=True)
    Full_name = models.CharField(max_length=55)
    otp = models.CharField(max_length=6)
    username = None
    first_name = None
    last_name= None
    def __str__(self):
        return self.Full_name

    object = CustomUserManager()
   




