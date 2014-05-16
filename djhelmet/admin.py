from django.contrib import admin
from djhelmet.models import Product, Size, Colors, Product_colors, Product_size, Images
# Register your models here.

#
#class ImagesInline(admin.TabularInline):
#    model=Images
#    extra =1
#    max_num=7
#
#class ProductAdmin(admin.ModelAdmin):
#    inlines       = (ImagesInline,)

#admin.site.register(Product,ProductAdmin)
admin.site.register(Product)
admin.site.register(Images)
admin.site.register(Size)
admin.site.register(Colors)
admin.site.register(Product_colors)
admin.site.register(Product_size)
