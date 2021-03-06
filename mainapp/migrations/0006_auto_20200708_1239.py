# Generated by Django 2.2 on 2020-07-08 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0005_productcategory_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='is_active'),
        ),
        migrations.AlterField(
            model_name='productcategory',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='is_active'),
        ),
    ]
