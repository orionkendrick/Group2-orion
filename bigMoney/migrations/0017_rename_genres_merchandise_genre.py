# Generated by Django 4.2 on 2023-04-21 23:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bigMoney', '0016_merchandise_genres_alter_cartitem_quantity'),
    ]

    operations = [
        migrations.RenameField(
            model_name='merchandise',
            old_name='genres',
            new_name='genre',
        ),
    ]