# Generated by Django 3.0.2 on 2020-02-04 21:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0003_auto_20200204_2149'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='DeliveryCharges',
            new_name='DeliveryCharge',
        ),
    ]
