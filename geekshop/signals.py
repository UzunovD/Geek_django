from django.db.models.signals import pre_save, pre_delete
from django.dispatch import receiver

from basketapp.models import Basket
from my_ordersapp.models import OrderItem


@receiver(pre_save, sender=OrderItem)
@receiver(pre_save, sender=Basket)
def product_quantity_update_save(sender, update_fields, instance, **kwargs):
    if instance.pk:
        instance.product.quantity -= instance.quantity - sender.get_item(instance.pk).quantity
    else:
        instance.product.quantity -= instance.quantity
    instance.product.save()


@receiver(pre_delete, sender=OrderItem)
@receiver(pre_delete, sender=Basket)
def product_quantity_update_save(sender, update_fields, instance, **kwargs):
    instance.product.quantity += instance.quantity
    instance.product.save()
