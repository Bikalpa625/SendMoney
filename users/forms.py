from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=100)
    middle_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    username = forms.CharField(max_length=100  )
    email = forms.EmailField()
    street_address = forms.CharField(max_length=255)
    city = forms.CharField(max_length=100)
    state = forms.CharField(max_length=100)
    zip_code = forms.CharField(max_length=10)
    mobile_number = forms.CharField(max_length=15)
    

    class Meta:
        model=User
        fields=['first_name','middle_name','last_name','username','password1','password2','email','street_address','city','state','zip_code','mobile_number']




