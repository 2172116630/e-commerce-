from django.urls import path
from. import views

path('<slug:slug>/', views.product_comment, name='product_comment')