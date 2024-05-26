from django.contrib import admin
from .models import ContactMessage

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'contact_number', 'message', 'created_at')
    list_filter = ('created_at', 'email')
    search_fields = ('first_name', 'last_name', 'email', 'contact_number')
