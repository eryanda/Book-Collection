# Generated by Django 4.2.5 on 2023-09-19 11:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_product_title'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='name',
            new_name='genre',
        ),
    ]
