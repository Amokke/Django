from django.core.management.base import BaseCommand
from django.utils.timezone import now
from decimal import Decimal
import random

from GBDS.shop.models import Client, Product, Order


class Command(BaseCommand):
    help = 'Заполнение баз случайными данными'

    def handle(self, *args, **kwargs):
        clients = [Client.objects.create(
            name=f'Client {i}',
            email=f'client{i}test.ru',
            phone_number=f'8908888888{i}',
            address=f'Улица {i}'
        ) for i in range(1, 6)]

        products = [Product.objects.create(
            name=f'Product {i}',
            description=f'Description for Product {i}',
            price=Decimal(random.uniform(10, 100)),
            quantity=random.randint(1, 10)
        ) for i in range(1, 11)]

        for i in range(1, 6):
            client = random.choice(clients)
            products_in_order = random.sample(products, random.randint(1, 5))
            total_amount = sum(product.price * product.quantity for product in products_in_order)
            order = Order.objects.create(
                client=client,
                total_amount=total_amount,
                order_date=now()
            )
            order.products.set(products_in_order)

        self.stdout.write(self.style.SUCCESS('Все базы созданы успешно'))
