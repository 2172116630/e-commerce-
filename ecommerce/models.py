from django.db import models
from django.conf import settings
# Create your models here.
class Category(models.Model):
  STATUS = (
    ('True', 'True'),
    ('False', 'False'),
    )
    
  title = models.CharField(max_length=50)
    
  body = models.TextField(max_length=255)
  #image=models.ImageField(blank=True,upload_to='images/')
  status=models.CharField(max_length=10, choices=STATUS)
  create_on=models.DateTimeField(auto_now_add=True)
  update_on=models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.title


class Product(models.Model):
  STATUS = (
    ('True', 'True'),
    ('False', 'False'),
    )

  VARIANTS = (
    ('None', 'None'),
    ('Size', 'Size'),
    ('Color', 'Color'),
    ('Size-Color', 'Size-Color'),

    )
  category = models.ForeignKey(Category, on_delete=models.CASCADE) #many to one relation with Category
  title = models.CharField(max_length=150)
  body = models.TextField(max_length=255)
  #image=models.ImageField(upload_to='images/',null=False)
  price = models.DecimalField(max_digits=12, decimal_places=2, default=0)
  variant=models.CharField(max_length=10,choices=VARIANTS, default='None')
  slug = models.SlugField(null=False, unique=True)
  status=models.CharField(max_length=10,choices=STATUS)
  create_on=models.DateTimeField(auto_now_add=True)
  update_on=models.DateTimeField(auto_now=True)
  
  def __str__(self):
    return self.title

class Comment(models.Model):
  STATUS = (
    ('New', 'New'),
    ('True', 'True'),
    ('False', 'False'),
    )
  product=models.ForeignKey(Product,on_delete=models.CASCADE)
  comment = models.CharField(max_length=250,blank=True)
  title = models.CharField(max_length=20, blank=True)
  status=models.CharField(max_length=10,choices=STATUS, default='New')
  create_on=models.DateTimeField(auto_now_add=True)
  update_on=models.DateTimeField(auto_now=True)

  
  def __str__(self):
    return self.title 

class ProductBasket (models.Model):
  product=models.ForeignKey(Product,on_delete=models.CASCADE)
  title = models.CharField(max_length=20, blank=True)
  quantity=models.IntegerField(default=1)


  def __str__(self):
    return self.title

class Order (models.Model):
  user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  product=models.ManyToManyField(ProductBasket)
  create_on=models.DateTimeField(auto_now_add=True)
  order_date=models.DateTimeField
  ordered=models.BooleanField(default=False)
  quantity=models.IntegerField(default=1)


  def __str__(self):
    return self.username

class About(models.Model):
  title= models.CharField(max_length=50)
  body=models.TextField(max_length=255)



  