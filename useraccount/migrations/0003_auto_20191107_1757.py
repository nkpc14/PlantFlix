# Generated by Django 2.2.6 on 2019-11-07 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('useraccount', '0002_useraccount_profile_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraccount',
            name='courses',
            field=models.ManyToManyField(blank=True, to='course.Course'),
        ),
        migrations.AlterField(
            model_name='useraccount',
            name='mobile',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='useraccount',
            name='profile_photo',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
