# Generated by Django 3.2.3 on 2021-12-12 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0019_alter_appointment_more_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='Index',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video', models.FileField(null=True, upload_to='videos/', verbose_name='')),
            ],
            options={
                'verbose_name': 'video',
            },
        ),
    ]
