from django.db import models
from select_multiple_field.models import SelectMultipleField

class User_g(models.Model):

    mass = (("s","lol"),("n","d"))
    POST = SelectMultipleField(
        max_length=10,
        choices=mass
    )