# Generated by Django 3.2.6 on 2021-08-06 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='productincart',
            name='ordered',
            field=models.BooleanField(default=False),
        ),
    ]
