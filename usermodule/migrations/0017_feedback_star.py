# Generated by Django 5.0.1 on 2024-03-10 01:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usermodule', '0016_remove_feedback_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='star',
            field=models.CharField(default=1, max_length=25),
            preserve_default=False,
        ),
    ]
