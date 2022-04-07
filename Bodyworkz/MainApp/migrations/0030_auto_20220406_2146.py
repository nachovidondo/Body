# Generated by Django 3.2.3 on 2022-04-06 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0029_appointment_time_available'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='time',
            field=models.CharField(blank=True, choices=[('15:00', '15:00'), ('16:00', '16:00'), ('17:00', '17:00'), ('18:00', '18:00'), ('19:00', '19:00'), ('20:00', '20:00')], max_length=255, null=True, verbose_name='Time'),
        ),
    ]
