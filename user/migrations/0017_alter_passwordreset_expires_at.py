# Generated by Django 5.1.4 on 2025-01-13 03:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0016_alter_passwordreset_expires_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='passwordreset',
            name='expires_at',
            field=models.DateTimeField(default=datetime.datetime(2025, 1, 13, 8, 53, 30, 18128)),
        ),
    ]
