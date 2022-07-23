from django import forms
from .models import ToDo
from django.core.exceptions import ValidationError
from django.contrib.admin.widgets import AdminDateWidget

class ToDoForm(forms.ModelForm):
    class Meta:
        model = ToDo
        fields = ['title', 'status', 'due_date']


