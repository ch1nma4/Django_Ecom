# Generated by Django 4.2.7 on 2023-12-04 14:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Ecommerce', '0004_alter_order_complete_alter_order_customer'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderitem',
            old_name='Product',
            new_name='product',
        ),
    ]
