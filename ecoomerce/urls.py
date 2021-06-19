from django.urls import path
from . import views

urlpatterns = [
    path('available/', views.available_product),
    path('unavailable/', views.unavailable_poduct),

]