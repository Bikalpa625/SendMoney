# money_transfer/forms.py
from django import forms
from .models import Transaction

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
