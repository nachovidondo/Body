# Generated by Django 3.1.3 on 2021-10-12 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0006_therapist_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='therapist',
            name='description',
            field=models.TextField(default='R'),
        ),
    ]
