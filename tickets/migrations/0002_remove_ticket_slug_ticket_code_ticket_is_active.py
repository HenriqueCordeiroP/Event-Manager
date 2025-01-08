# Generated by Django 5.1.4 on 2025-01-08 04:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticket',
            name='slug',
        ),
        migrations.AddField(
            model_name='ticket',
            name='code',
            field=models.CharField(blank=True, max_length=15, unique=True),
        ),
        migrations.AddField(
            model_name='ticket',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
    ]
