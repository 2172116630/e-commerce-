from django.urls import path
from .views import available_product, unavailable_product, product_detail, product_comment, add_to_cart, remove_from_cart, about_view 

app_name = 'ecommerce'
urlpatterns = [
    path('available/', available_product),
    path('unavailable/', unavailable_product),
    path('show/product/<int:product_id>/', product_detail),
    path('<slug:slug>/', product_comment, name='product_comment')
    path('add-to-cart/<slug>/', add_to_cart, name='add_to_cart'),
    path('remove-from-cart/<slug>/', remove_from_cart, name='remove-from-cart'),
    path('about/', about_view),

]


