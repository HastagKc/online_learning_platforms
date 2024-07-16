from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUserModel(AbstractUser):
    gender = models.CharField(max_length=200)
    is_teacher = models.BooleanField(default=False)

# # Create your models here.


# class StudentModel(models.Model):
#     first_name = models.CharField(max_length=200)
#     last_name = models.CharField(max_length=200)
#     email = models.EmailField()
#     is_student = models.BooleanField(default=False)
#     username = models.CharField(max_length=200)
#     password = models.CharField(max_length=200)

#     def __str__(self):
#         return f'{self.first_name} + {self.last_name}'


# class TeacherModel(models.Model):
#     first_name = models.CharField(max_length=200)
#     last_name = models.CharField(max_length=200)
#     email = models.EmailField()
#     is_teacher = models.BooleanField(default=False)
#     username = models.CharField(max_length=200)
#     password = models.CharField(max_length=200)

#     def __str__(self):
#         return f'{self.first_name} + {self.last_name}'


# class AboutTeacher(models.Model):
#     profile_img = models.ImageField(upload_to='profile', blank=True, null=True)
#     about = models.CharField(max_length=200, default=None)
#     address = models.CharField(max_length=200, default=None)
#     teacher = models.OneToOneField(TeacherModel, on_delete=models.CASCADE)
