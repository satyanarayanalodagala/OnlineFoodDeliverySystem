# Generated by Django 5.0.1 on 2024-03-08 05:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usermodule', '0011_alter_order_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='food',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usermodule.add_food'),
        ),
        migrations.AlterField(
            model_name='order',
            name='res',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usermodule.resturent_signup'),
        ),
    ]
