from django import forms
from main.models import Author
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UpdateForm(forms.ModelForm):
    
    class Meta:
        model = Author
        fields = ("fullname", "bio","email", "profile_pic",)

