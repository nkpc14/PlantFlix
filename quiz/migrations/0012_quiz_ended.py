# Generated by Django 2.2.6 on 2019-11-07 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0011_auto_20191106_2345'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiz',
            name='ended',
            field=models.BooleanField(blank=True, default=False),
        ),
    ]