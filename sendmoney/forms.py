# money_transfer/forms.py
from django import forms







class ContactForm(forms.Form):
    first_name = forms.CharField(label='First Name', max_length=100)
    last_name = forms.CharField(label='Last Name', max_length=100)
    email = forms.EmailField(label='Email')
    contact_number = forms.CharField(label='Contact Number', max_length=15)
    message = forms.CharField(label='Message', widget=forms.Textarea)

