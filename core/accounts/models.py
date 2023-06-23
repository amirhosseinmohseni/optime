from django.db import models
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser, PermissionsMixin)
from django.utils.translation import gettext_lazy as _
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.exceptions import ValidationError
import re


def validate_phone(value):
    """
        this function is for validate phone number and set with 
        regex template.
    """
    regex = re.match("09(1[0-9]|3[1-9]|2[1-9])-?[0-9]{3}-?[0-9]{4}", value)
    if regex:
        return regex.group()
    else:
        raise ValidationError("Please add valid phone number")


class UserManager(BaseUserManager):
    """
        custom manager for the user model 
    """
    def create_user(self, phone, password, **extra_fields):
        if not phone:
            raise ValueError(_("phone must be set"))
        user = self.model(phone=phone, **extra_fields)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, phone, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        
        if extra_fields.get('is_staff') is not True:
            raise ValueError(_("superuser must have 'is_staff=True'"))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_("superuser must have 'is_superuser=True'"))
        return self.create_user(phone, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    """
        custom user model for the project
    """
    phone = models.CharField(max_length=11, unique=True, validators=[validate_phone])
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_verified = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
    objects = UserManager()
    
    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = []
    
    def __str__(self):
        return self.phone
    
class CourierManager(BaseUserManager):
    """
        custom manager for the courier model 
    """
    def create_user(self, phone, password, **extra_fields):
        if not phone:
            raise ValueError(_("phone must be set"))
        user = self.model(phone=phone, **extra_fields)
        user.set_password(password)
        user.save()
        return user

class Courier(User):
    """
        custom courier model that inherits from User 
    """
    is_superuser = None
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    is_available = models.BooleanField(default=True)
    
    objects = CourierManager()