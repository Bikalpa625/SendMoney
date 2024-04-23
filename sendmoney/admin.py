from django.contrib import admin
from .models import Country
from .models import Transaction


admin.site.register(Country)
admin.site.register(Transaction)

