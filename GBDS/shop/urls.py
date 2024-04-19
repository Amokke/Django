from django.urls import path
from .views import index, client_orders, about

app_name = 'shop'

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('client_orders/<int:client_id>/', client_orders, name='client_orders'),
]
