# Generated by Django 2.2.7 on 2019-11-27 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AttedanceManager', '0002_auto_20191126_1303'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='rfid',
            field=models.CharField(default='RFID tag not assigned', max_length=12),
        ),
    ]
