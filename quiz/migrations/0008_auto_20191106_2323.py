# Generated by Django 2.2.6 on 2019-11-06 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0007_auto_20191106_2322'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useranswer',
            name='answer',
            field=models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')], max_length=10, primary_key=True, serialize=False, unique=True),
        ),
    ]