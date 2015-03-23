# -*- coding: utf-8 -*-
from django.forms import Form
from django import forms
from select_multiple_field.forms import SelectMultipleFormField
from django.forms import Textarea

class Group_List(Form):

    def __init__(self, mylist, *args, **kwargs):
        super(self.__class__, self).__init__(*args, **kwargs)
        self.fields['POST'].choices = mylist

    POST = SelectMultipleFormField(
        max_length=10,
        choices=[],
    )
    Text = forms.CharField(widget=forms.Textarea(attrs={'rows':4}))
