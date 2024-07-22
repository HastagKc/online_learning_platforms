from django.db import models
from accounts.models import CustomUserModel
from django.core.validators import MinLengthValidator

# Create your models here.


class TeacherProfile(models.Model):
    user = models.ForeignKey(
        CustomUserModel, on_delete=models.CASCADE, related_name='Users')
    profile_img = models.ImageField(upload_to='profile_img')
    bio = models.TextField()
    age = models.PositiveIntegerField()
    address = models.CharField(max_length=200)
    phone_number = models.CharField(
        max_length=12,
        validators=[
            MinLengthValidator(
                10,
                message="Phone Number should be 10 charcter long",
            ),
        ],
    )
