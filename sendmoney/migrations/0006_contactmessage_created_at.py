# Generated by Django 5.0.4 on 2024-05-26 13:16

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sendmoney', '0005_contactmessage_delete_testimonial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactmessage',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]