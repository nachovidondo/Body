# Generated by Django 3.1.3 on 2021-11-17 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0010_auto_20211117_0524'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='therapy',
            name='therapist',
        ),
        migrations.AddField(
            model_name='therapy',
            name='therapist',
            field=models.ManyToManyField(to='MainApp.Therapist', verbose_name='Terapeuta'),
        ),
    ]
