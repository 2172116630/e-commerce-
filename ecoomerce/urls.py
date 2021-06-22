from django.urls import path
from .views import available_product, unavailable_poduct, product_detail

app_name = 'ecommerce'
urlpatterns = [
    path('available/', available_product),
    path('unavailable/', unavailable_poduct),
    path('show/product/<int:product_id>/', product_detail),

]

