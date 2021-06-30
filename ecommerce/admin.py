from django.contrib import admin
from .models import  Product, Comment, Category,ProductBasket, Order


# Register your models here.
class ProductAdmin(admin.ModelAdmin):
  pass
  #list_display = ('category', 'body', 'price', 'variant', 'slug', 'status', 'created_on', 'updated_on')
  #list_filter = ('updated_on', 'created_on', 'category')

  #def __str__(self):
    #return self.title
  

class CategoryAdmin(admin.ModelAdmin):
  pass
  #list_display = ('title', 'body', 'created_on', 'updated_on')
  #list_filter = ('updated_on', 'created_on')
  #search_fields = ['title', 'body']


class CommentInline(admin.TabularInline):
  #model = Comment
  pass

class CommentAdmin(admin.ModelAdmin):
  pass
  
 #list_display = ('comment', 'title', 'product', 'created_on', 'updated_on', 'status')
 #list_filter = ('updated_on', 'created_on')
 #search_fields = ['name', 'body']
 #actions = ['approve_comments']
 #inlines = [CommentInline,]


 #def approve_comments(self, request, queryset:
   #queryset.update(active=True)



admin.site.register(Product, ProductAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(ProductBasket)
admin.site.register(Order)
