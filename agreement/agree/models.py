
# Create your models here.

# users/models.py

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from .choice import *

class UserManager(BaseUserManager):
    def create_user(self, user_id, password, email, hp, name, student_id, grade, department, circles, auth, **extra_fields):
        user = self.model(
            user_id = user_id,
            email = email,
            hp = hp,
            name = name,
            student_id = student_id,
            grade = grade,
            department = department,
            circles = circles,
            auth = auth,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, user_id, password, email=None, hp=None, name=None, student_id=None, grade=None, department=None, circles=None, auth=None):
        user = self.create_user(user_id, password, email, hp, name, student_id, grade, department, circles, auth)
        user.is_superuser = True
        user.is_staff = True
        user.is_admin = True
        user.level = 0
        user.save(using=self._db)
        return user