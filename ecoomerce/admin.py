from django.contrib import admin
from .models import  Product, Comment, Category,ProductBasket, order


# Register your models here.
class ProductAdmin(admin.ModelAdmin):
  pass

class CategoryAdmin(admin.ModelAdmin):
  pass



class CommentAdmin(admin.ModelAdmin):
  pass
 # list_display = ('name', 'body', 'product', 'created_on', 'updated_on')
 # list_filter = ('updated_on', 'created_on')
 # search_fields = ('name', 'body')
 # actions = ['approve_comments']

 # def approve_comments(self, request, queryset:
 #   queryset.update(active=True)


admin.site.register(Product, ProductAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(ProductBasket)
admin.site.register(order)
