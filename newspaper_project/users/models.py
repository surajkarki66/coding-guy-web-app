from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class CustomUser(AbstractUser):                # Class for custom user.
    
    age = models.PositiveIntegerField(null=True, blank=True)