from .views import view_returns, cart, add_to_cart, product, products_list, add_product, edit_product, return_product
from django.urls import path

urlpatterns = [
    path('products_list/', products_list, name='products_list'),
    path('product/<int:product_id>/', product, name='product'),
    path('add_product/', add_product, name='add_product'),
    path('cart/', cart, name='cart'),
    path('add_to_cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('edit_product/<int:product_id>/', edit_product, name='edit_product'),
    path('return_product/<int:purchase_id>/', return_product, name='return_product'),
    path('view_returns/', view_returns, name='view_returns'),
]