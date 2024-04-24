# money_transfer/forms.py
from django import forms
from .models import Transaction
from .models import Testimonial


class TransactionForm(forms.ModelForm):
    PAYMENT_CHOICES = [
        ('account','Account Payment'),
        ('cash','Cash'),
    ]
    
 
    payment_method = forms.ChoiceField(choices=PAYMENT_CHOICES, widget=forms.RadioSelect)
    class Meta:
        model = Transaction
        fields = ['sender_country', 'receiver_country', 'amount']
        exclude = ['payment_method']

class ContactForm(forms.Form):
    first_name = forms.CharField(label='First Name', max_length=100)
    last_name = forms.CharField(label='Last Name', max_length=100)
    email = forms.EmailField(label='Email')
    contact_number = forms.CharField(label='Contact Number', max_length=15)
    message = forms.CharField(label='Message', widget=forms.Textarea)

class TestimonialForm(forms.ModelForm):
    class Meta:
        model = Testimonial
        fields = ['author', 'content']