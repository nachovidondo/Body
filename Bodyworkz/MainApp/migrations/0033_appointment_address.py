# Generated by Django 3.1.3 on 2022-04-09 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0032_time_available_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='address',
            field=models.CharField(default='----', max_length=255),
        ),
    ]
