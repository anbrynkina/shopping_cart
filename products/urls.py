# creating urls.py for products since in future for each product we would like us to redirect to a separate page like
# products/product_id ...

from django.urls import path
from products.views import products

app_name = 'products'

urlpatterns = [
    path('', products, name='index'),
]
