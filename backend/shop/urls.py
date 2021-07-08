from django.urls import path

from .views import ProductList


app_name = 'shop'

urlpatterns = [
    path('', ProductList.as_view(), name='product_list'),
]