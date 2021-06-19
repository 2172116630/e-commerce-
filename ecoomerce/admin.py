from django.contrib import admin


from .models import  Product, Comment, Category,ProductBasket, order


# Register your models here.
class ProductAdmin(admin.ModelAdmin):
  pass

class CategoryAdmin(admin.ModelAdmin):
  pass


admin.site.register(Product, ProductAdmin)
admin.site.register(Comment)
admin.site.register(Category, CategoryAdmin)
admin.site.register(ProductBasket)
admin.site.register(order)
