# Generated by Django 5.1.4 on 2025-01-13 19:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0021_remove_wallet_welcome_bonus_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='passwordreset',
            name='expires_at',
            field=models.DateTimeField(default=datetime.datetime(2025, 1, 14, 1, 39, 7, 23345)),
        ),
    ]
