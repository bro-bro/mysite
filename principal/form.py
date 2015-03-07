from django.forms import ModelForm
from django.db import models
from select_multiple_field.models import SelectMultipleField

class User_g(models.Model):

    mass = (("s","lol"),("n","d"))
    POST = SelectMultipleField(
        max_length=10,
        choices=mass
    )

class Group_List(ModelForm):
    massive = ""
    class Meta:
        model = User_g
        fields = ['POST']

