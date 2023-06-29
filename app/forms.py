from django.forms import ModelForm
from .models import ToDo


class TODOForm(ModelForm):
    class Meta:
        model = ToDo
        fields = ("title", "status" , "priority")
