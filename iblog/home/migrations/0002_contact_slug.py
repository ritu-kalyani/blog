# Generated by Django 3.0.7 on 2020-07-14 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='slug',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
