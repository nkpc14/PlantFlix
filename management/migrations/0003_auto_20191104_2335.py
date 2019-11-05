# Generated by Django 2.2.6 on 2019-11-04 18:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('management', '0002_auto_20191104_2331'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='messages',
            name='users',
        ),
        migrations.AddField(
            model_name='messages',
            name='users',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]