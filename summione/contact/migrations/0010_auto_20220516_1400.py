# Generated by Django 3.2.8 on 2022-05-16 08:30

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contact', '0009_auto_20220516_1342'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='likes',
            field=models.ManyToManyField(blank=True, default=None, related_name='likes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='contact',
            name='likes_count',
            field=models.BigIntegerField(default='0'),
        ),
    ]
