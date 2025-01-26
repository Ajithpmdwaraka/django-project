from django.contrib import admin
from .models import Category, Product, Order

# Register the Category model
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'category_name', 'description')
    search_fields = ('category_name',)
    ordering = ('id',)


# Register the Product model
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'product_name', 'category', 'price', 'description')
    list_filter = ('category',)
    search_fields = ('product_name', 'category__category_name')
    ordering = ('id',)


# Register the Order model
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer_name', 'customer_email', 'product', 'quantity')
    list_filter = ('product',)
    search_fields = ('customer_name', 'customer_email', 'product__product_name')
    ordering = ('id',)
