# money_transfer/models.py
from django.db import models
from django.utils import timezone

class Country(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Transaction(models.Model):
    sender_country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='sent_transactions')
    receiver_country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='received_transactions')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)

class Testimonial(models.Model):
    author = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.author

