from rest_framework import serializers
from .models import Category, Product, Order


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'category_name', 'description']


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)  # Nested serializer for category
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(), write_only=True, source='category'
    )

    class Meta:
        model = Product
        fields = [
            'id', 
            'product_name', 
            'description', 
            'price', 
            'image', 
            'category', 
            'category_id'
        ]


class OrderSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)  # Nested serializer for product
    product_id = serializers.PrimaryKeyRelatedField(
        queryset=Product.objects.all(), write_only=True, source='product'
    )

    class Meta:
        model = Order
        fields = [
            'id', 
            'customer_name', 
            'customer_email', 
            'product', 
            'product_id', 
            'quantity'
        ]
