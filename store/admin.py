# Register your models here.
from django.contrib import admin
from .models import Product, Sale



@admin.register(Sale)
class SaleAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'quantity', 'timestamp')
    list_filter = ('timestamp', 'user', 'product')

admin.site.register(Product)


