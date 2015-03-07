from django.forms import ModelForm
from models import User_g

class Group_List(ModelForm):
    massive = ""
    class Meta:
        model = User_g
        fields = ['POST']

