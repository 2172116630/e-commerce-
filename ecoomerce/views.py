from django.shortcuts import render
from .mpdels import Product
# Create your views here.
def available_product(request):
  data={}
  poll_list = Product.objects.filter(status=True)
  data['available'] = poll_list
  return render(request, "available_product.html", context=data)

def unavailable_product(request):
  data={}
  poll_list = Product.objects.filter(status=False)
  data['unavailable'] = poll_list
  return render(request, "unavailable_product.html", context=data)