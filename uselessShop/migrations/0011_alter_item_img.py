# Generated by Django 4.2.13 on 2024-05-09 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uselessShop', '0010_alter_item_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='img',
            field=models.ImageField(default=None, upload_to='images/'),
        ),
    ]
