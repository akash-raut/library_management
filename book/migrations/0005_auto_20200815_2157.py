# Generated by Django 3.1 on 2020-08-15 16:27

from django.db import migrations
import phone_field.models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0004_auto_20200815_2018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='contact',
            field=phone_field.models.PhoneField(blank=True, max_length=10),
        ),
    ]
