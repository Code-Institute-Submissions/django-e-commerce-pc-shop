# Generated by Django 3.1.6 on 2021-02-17 07:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_auto_20210203_1222'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='promo_side_banner_bottom',
        ),
    ]