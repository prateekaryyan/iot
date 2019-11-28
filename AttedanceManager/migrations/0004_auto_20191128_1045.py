# Generated by Django 2.2.7 on 2019-11-28 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AttedanceManager', '0003_teacher_rfid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='status',
            field=models.BooleanField(default='False'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='rfid',
            field=models.IntegerField(default='Not assigned'),
        ),
    ]
