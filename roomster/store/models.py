from django.db import models
import datetime

# Create your models here.
class Space(models.Model):
    location = models.CharField(max_length=255)
    price = models.FloatField()
    description = models.CharField(max_length=1000)
    photo = models.ImageField(upload_to='space')
    entry_date = models.DateTimeField(default=datetime.datetime.now)
    is_negotiable = models.BooleanField()
    is_expired = models.BooleanField(default=False)

class Facility(models.Model):
    name = models.CharField(max_length=255)
    space = models.ForeignKey(
        Space,
        on_delete=models.CASCADE,
        related_name="facility"
    )

class Furniture(models.Model):
    types = models.CharField(max_length=255)
    price = models.FloatField()
    description = models.CharField(max_length=1000)
    photo = models.ImageField(upload_to='furniture')
    entry_date = models.DateTimeField(default=datetime.datetime.now)
    used_period = models.CharField(max_length=100)
    is_negotiable = models.BooleanField()
    is_expired = models.BooleanField(default=False)
    is_like_new = models.BooleanField()
    