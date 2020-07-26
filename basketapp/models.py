from authapp.models import ShopUser
from django.db import models
from mainapp.models import Product


class Basket(models.Model):
    user = models.ForeignKey(ShopUser, on_delete=models.CASCADE, related_name='basket')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(verbose_name='amount', default=0)
    add_datetime = models.DateTimeField(verbose_name='time', auto_now_add=True)


    @property
    def product_cost(self):
        '''return cost of all products this type'''
        return self.product.price * self.quantity


    @property
    def total_quantity(self):
        '''return total quantity of user'''
        _items = self.user.basket.all()
        _total_quantity = sum(map(lambda item: item.quantity, _items))
        return _total_quantity

    @property
    def total_cost(self):
        '''return total cost of all items for user'''
        _items = self.user.basket.all()
        _total_cost = sum(map(lambda item: item.product_cost, _items))
        return _total_cost
