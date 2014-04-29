from django.contrib import admin
from djhelmet.models import Product, Size, Colors, Product_colors, Product_size, Images
# Register your models here.


admin.site.register(Product)
admin.site.register(Size)
admin.site.register(Colors)
admin.site.register(Product_colors)
admin.site.register(Product_size)
admin.site.register(Images)