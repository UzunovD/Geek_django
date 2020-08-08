from django.utils.functional import cached_property

from authapp.models import ShopUser
from django.db import models
from mainapp.models import Product


# class BasketQuerySet(models.QuerySet):
#     def delete(self):
#         for object in self:
#             object.delete()
#         return super(BasketQuerySet, self).delete()


class Basket(models.Model):
    user = models.ForeignKey(ShopUser, on_delete=models.CASCADE, related_name='basket')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(verbose_name='amount', default=0)
    add_datetime = models.DateTimeField(verbose_name='time', auto_now_add=True)

    # objects = BasketQuerySet.as_manager()

    @cached_property
    def get_items_cashed(self):
        return self.user.basket.select_related('product').all()

    @property
    def product_cost(self):
        '''return cost of all products this type'''
        return self.product.price * self.quantity

    @property
    def total_quantity(self):
        '''return total quantity of user'''
        _items = self.get_items_cashed
        _total_quantity = sum(map(lambda item: item.quantity, _items))
        return _total_quantity

    @property
    def total_cost(self):
        '''return total cost of all items for user'''
        _items = self.get_items_cashed
        _total_cost = sum(map(lambda item: item.product_cost, _items))
        return _total_cost

    @staticmethod
    def get_item(pk):
        return Basket.objects.get(pk=pk)


    # def delete(self, using=None, keep_parents=False):
    #     self.product.quantity += self.quantity
    #     self.product.save()
    #     return super().delete(using=None, keep_parents=False)

