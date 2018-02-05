from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.


class User(AbstractUser):
    '''
    Extending django built in roles
    '''
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)
    full_name = models.CharField(max_length=50)


class Student(models.Model):
    '''
    Adding custom fields for user
    '''
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    fathers_name = models.CharField(max_length=50)
    mothers_name = models.CharField(max_length=50)

    def __str__(self):
        return self.user.username


class Teacher(models.Model):
    '''
    Adding custom fields for user
    '''
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    subject = models.CharField(max_length=20)

    def __str__(self):
        return self.user.username
