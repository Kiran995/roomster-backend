from django.db import models
import datetime
from multiselectfield import MultiSelectField

# Create your models here.
class Space(models.Model):
    FACILITY_CHOICES = (
        ('24 hr WATER', '24 hr WATER'),
        ('NEAR ROAD', 'NEAR ROAD'),
        ('TRANSPORTATION', 'TRANSPORTATION'),
        ('INTERNET', 'INTERNET'),
        ('HOT WATER', 'HOT WATER'),
        ('SECURITY GUARD', 'SECURITY GUARD'),
        ('CAR PARKING SPACE', 'CAR PARKING SPACE'),
        ('BIKE PARKING SPACE', 'BIKE PARKING SPACE')
    )
    location = models.CharField(max_length=255)
    price = models.FloatField()
    description = models.CharField(max_length=1000)
    # photo = models.ImageField(upload_to='upload/space')
    entry_date = models.DateTimeField(default=datetime.datetime.now)
    is_negotiable = models.BooleanField()
    is_expired = models.BooleanField(default=False)
    facility = MultiSelectField(choices=FACILITY_CHOICES)

class Furniture(models.Model):
    types = models.CharField(max_length=255)
    price = models.FloatField()
    description = models.CharField(max_length=1000)
    # photo = models.ImageField(upload_to='upload/furniture')
    entry_date = models.DateTimeField(default=datetime.datetime.now)
    used_period = models.CharField(max_length=100)
    is_negotiable = models.BooleanField()
    is_expired = models.BooleanField(default=False)
    is_like_new = models.BooleanField()

class Image(models.Model):
    space = models.ForeignKey(
        Space, 
        related_name="space_images", 
        null=True, 
        blank=True,
        on_delete=models.CASCADE
    )
    furniture = models.ForeignKey(
        Furniture, 
        related_name="furniture_images", 
        null=True, 
        blank=True,
        on_delete=models.CASCADE
    )
    image = models.ImageField()
    