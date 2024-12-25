# Generated by Django 5.1.4 on 2024-12-25 19:21

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_alter_event_id'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='attendants',
            field=models.ManyToManyField(blank=True, related_name='attended_events', to=settings.AUTH_USER_MODEL),
        ),
    ]
