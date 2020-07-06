from django.db import models


class ProductCategory(models.Model):
    name = models.CharField('category name', max_length=50)
    description = models.TextField('category description', blank=True)
    is_active = models.BooleanField(verbose_name='активна', default=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField('product name', max_length=100)
    category = models.ForeignKey(ProductCategory, models.CASCADE, verbose_name='category of product')
    type_prod = models.CharField('type of product', max_length=50, blank=True, null=True)
    description = models.TextField('product description', blank=True)
    short_desc = models.CharField('short descriotion', max_length=50, blank=True)
    price = models.DecimalField('Price', max_digits=8, decimal_places=2, default=0)
    image = models.ImageField(upload_to='products_images', blank=True)
    quantity = models.PositiveIntegerField('quantity', default=0)

    def __str__(self):
        return f'{self.name} ({self.category.name})'
