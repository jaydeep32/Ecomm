# Generated by Django 3.2.5 on 2021-08-03 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('is_popular', models.BooleanField(default=False)),
                ('created_at', models.DateField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'categories',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('description', models.TextField()),
                ('pic', models.ImageField(upload_to='products')),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('is_active', models.BooleanField(default=True)),
                ('is_discount', models.BooleanField(default=False)),
                ('discount', models.IntegerField(default=0)),
                ('created_at', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
