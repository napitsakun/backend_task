# from django.db import models
from django.contrib.gis.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    country = models.CharField(max_length=100, null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    phone_number = models.CharField(max_length=25, null=True, blank=True)
    area_of_interest = models.TextField(null=True, blank=True)
    user_document = models.FileField(upload_to="documents/", null=True, blank=True)
    birthday = models.DateField(null=True, blank=True)
    home_address = models.PointField(null=True, blank=True)
    office_address = models.PointField(null=True, blank=True)

    REQUIRED_FIELDS = ["email", ]