# Generated by Django 2.2.6 on 2019-11-03 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0002_auto_20191103_1018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='correctOption',
            field=models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4)], max_length=10),
        ),
    ]