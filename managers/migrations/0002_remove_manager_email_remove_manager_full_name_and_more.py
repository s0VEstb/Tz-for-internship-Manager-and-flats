# Generated by Django 4.2.11 on 2024-04-11 09:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('managers', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='manager',
            name='email',
        ),
        migrations.RemoveField(
            model_name='manager',
            name='full_name',
        ),
        migrations.RemoveField(
            model_name='manager',
            name='password',
        ),
    ]
