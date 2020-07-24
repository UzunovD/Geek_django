from django.views.generic import ListView

from my_ordersapp.models import Order


class OrdersView(ListView):
    model = Order

    def get_queruset(self):
        return
