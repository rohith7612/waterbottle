# admin.py
from django.contrib import admin
from .models import Product, Sale
from .models import ProductImage

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category')  # Show category in product list
    list_filter = ('category',)  # Enable filtering by category in sidebar
    search_fields = ('name',)
    inlines = [ProductImageInline]

@admin.register(Sale)
class SaleAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'quantity', 'timestamp')
    list_filter = ('timestamp', 'user', 'product')
