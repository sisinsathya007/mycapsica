# Generated by Django 4.1.7 on 2023-08-03 11:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cart',
            old_name='cartid',
            new_name='cart_id',
        ),
        migrations.AlterModelTable(
            name='cartitem',
            table='CartItem',
        ),
    ]