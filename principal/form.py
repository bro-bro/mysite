from django.forms import Form
from select_multiple_field.forms import SelectMultipleFormField

class Group_List(Form):

    def __init__(self, mylist, *args, **kwargs):
        super(self.__class__, self).__init__(*args, **kwargs)
        self.fields['POST'].choices = mylist

    POST = SelectMultipleFormField(
        max_length=10,
        choices=[],
    )
        

    