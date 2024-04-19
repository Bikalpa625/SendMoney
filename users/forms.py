from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    firstname=forms.CharField()
    middlename=forms.CharField()
    lastname=forms.CharField()
    DOB=forms.DateField(required=False,input_formats='%d-%m-%Y')
    email=forms.EmailField()
    street_Address=forms.CharField()
    city=forms.CharField()
    state=forms.CharField()
    zipcode=forms.IntegerField()
    mobile_number=forms.IntegerField()

    class Meta:
        model=User
        fields=['firstname','middlename','lastname','DOB','username','password1','password2','email','street_Address','city','state','zipcode','mobile_number']




