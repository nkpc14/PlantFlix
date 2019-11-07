# Generated by Django 2.2.6 on 2019-11-06 18:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0010_auto_20191106_2331'),
    ]

    operations = [
        migrations.AddField(
            model_name='useranswer',
            name='id',
            field=models.AutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='useranswer',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz.Question'),
        ),
    ]