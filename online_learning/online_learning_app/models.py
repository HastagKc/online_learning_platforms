from django.db import models
from accounts.models import CustomUserModel

# Create your models here.


class Course(models.Model):
    user = models.ForeignKey(CustomUserModel, on_delete=models.CASCADE)
    course_title = models.CharField(max_length=200)
    
