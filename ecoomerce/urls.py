from django.urls import path
from .views import available_product, unavailable_poduct

app_name = 'ecommerce'
urlpatterns = [
    path('available/', available_product),
    path('unavailable/', unavailable_poduct),

]

