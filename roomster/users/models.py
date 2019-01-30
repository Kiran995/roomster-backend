from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    password = models.CharField(max_length=255)
    contact_no = models.IntegerField(max_length=15)
    citizenship_no = models.IntegerField(max_length=50)
    is_admin = models.BooleanField(default=False)