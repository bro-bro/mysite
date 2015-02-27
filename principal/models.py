
from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
   """model to represent additional information about users"""
   user = models.OneToOneField(User)
   # ... other custom stuff here