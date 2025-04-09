from django.contrib import admin
from .models import Product, ProductDetail, Tag

class ProductDetailInline(admin.TabularInline):
    model = ProductDetail
    extra = 1

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'quantity', 'price', 'user', 'created_at')
    list_filter = ('created_at', 'tags')
    search_fields = ('name', 'description')
    inlines = [ProductDetailInline]
    filter_horizontal = ('tags',)

@admin.register(ProductDetail)
class ProductDetailAdmin(admin.ModelAdmin):
    list_display = ('product', 'serial_number', 'expiry_date', 'created_at')
    list_filter = ('created_at', 'expiry_date')
    search_fields = ('serial_number', 'additional_info')

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)