# Generated by Django 5.1.4 on 2025-01-18 11:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0031_alter_passwordreset_expires_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='passwordreset',
            name='expires_at',
            field=models.DateTimeField(default=datetime.datetime(2025, 1, 18, 16, 43, 52, 91031)),
        ),
    ]
