# Generated by Django 3.0.7 on 2020-07-14 15:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_contact_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='slug',
        ),
    ]
