from django.shortcuts import render
from django.utils import timezone
from datetime import timedelta
from .models import Client, Product


def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def client_orders(request, client_id):
    client = Client.objects.get(pk=client_id)

    last_7_days = timezone.now() - timedelta(days=7)
    client_orders_7_days = Product.objects.filter(order_client=client,
                                                  order_date=last_7_days).distinct()

    last_30_days = timezone.now() - timedelta(days=30)
    client_orders_30_days = Product.objects.filter(order_client=client,
                                                   order_date=last_30_days).distinct()

    last_365_days = timezone.now() - timedelta(days=365)
    client_orders_365_days = Product.objects.filter(order_client=client,
                                                    order_date=last_365_days).distinct()

    return render(request, 'client_orders.html', {
        'client_orders_7_days': client_orders_7_days,
        'client_orders_30_days': client_orders_30_days,
        'client_orders_365_days': client_orders_365_days,
    })
