# Generated by Django 5.0.1 on 2024-02-17 17:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usermodule', '0005_add_food'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='add_food',
            name='user',
        ),
    ]
