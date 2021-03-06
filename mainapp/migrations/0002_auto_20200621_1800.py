# Generated by Django 2.2 on 2020-06-21 18:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productcategory',
            name='description',
            field=models.TextField(blank=True, verbose_name='category description'),
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='product name')),
                ('description', models.TextField(blank=True, verbose_name='product description')),
                ('short_desc', models.CharField(blank=True, max_length=50, verbose_name='short descriotion')),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=8, verbose_name='Price')),
                ('image', models.ImageField(blank=True, upload_to='products_images')),
                ('quantity', models.PositiveIntegerField(default=0, verbose_name='quantity')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.ProductCategory', verbose_name='category of product')),
            ],
        ),
    ]
