# Generated by Django 5.1.4 on 2024-12-18 03:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_alter_passwordreset_expires_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='passwordreset',
            name='expires_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 12, 18, 9, 31, 18, 732336)),
        ),
    ]
