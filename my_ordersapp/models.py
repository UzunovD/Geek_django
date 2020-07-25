from django.contrib.auth import get_user_model
from django.db import models

from authapp.models import ShopUser
from mainapp.models import Product


class Order(models.Model):
    FORMING = 'F'
    SENT_TO_PROCEED = 'S'
    PROCEEDED = 'O'
    PAID = 'P'
    READY = 'R'
    CANCEL = 'C'

    ORDER_STATUS_CHOICES = (
        (FORMING, 'is forming'),
        (SENT_TO_PROCEED, 'sent for processing'),
        (PAID, 'paid'),
        (PROCEEDED, 'is proceeding'),
        (READY, 'ready'),
        (CANCEL, 'cancel'),
    )

    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    created = models.DateTimeField(verbose_name='created', auto_now_add=True)
    updated = models.DateTimeField(verbose_name='updated', auto_now=True)
    status = models.CharField(verbose_name='sstatus', max_length=1, choices=ORDER_STATUS_CHOICES, default=FORMING)
    is_active = models.BooleanField(verbose_name='is active', default=True)

    class Meta:
        ordering = ('-created',)
        verbose_name = 'order'
        verbose_name_plural = 'orders'

    def __str__(self):
        return f'Current order: {self.id}'

    def get_total_quantity(self):
        items = self.orderitems.all()
        return sum(list(map(lambda x: x.quantity, items)))

    def get_product_type_quantity(self):
        items = self.orderitems.all()
        return len(items)

    def get_total_coast(self):
        items = self.orderitems.all()
        return sum(list(map(lambda x: x.quantity * x.product.price, items)))

    # def delete(self):
    #     for item in self.orderitems.select_related():
    #         item.product.quantity += item.quantity
    #         item.product.save()
    #
    #     self.is_active = False
    #     self.save()


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name="orderitems", on_delete=models.CASCADE)
    product = models.ForeignKey(Product, verbose_name='product', on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(verbose_name='quantity', default=0)

    @property
    def product_cost(self):
        return self.product.price * self.quantity