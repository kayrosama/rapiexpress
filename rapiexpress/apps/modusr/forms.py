from pyexpat import model
from attr import fields
from django import forms
from .models import Usuarios

class UserForm(forms.ModelForm):
    class Meta:
        model = Usuarios
        fields = '__all__'
     