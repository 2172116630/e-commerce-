from django.urls import path



from .views import available_product, unavailable_product, product_detail, product_comment

app_name = 'ecommerce'
urlpatterns = [
    path('available/', available_product),
    path('unavailable/', unavailable_product),
    path('show/product/<int:product_id>/', product_detail),
    path('<slug:slug>/', product_comment, name='product_comment')

]


