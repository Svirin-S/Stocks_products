from rest_framework import serializers

from .models import *


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title', 'description']


class StockProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = StockProduct
        fields = ['product', 'quantity', 'price']


class StockSerializer(serializers.ModelSerializer):
    positions = StockProductSerializer(read_only=True, many=True)

    class Meta:
        model = Stock
        fields = ['id', 'address', 'positions']
    
    def create(self, validated_data):
        positions = validated_data.pop('positions', [])
        stock_product = super().create(validated_data)
        for position in positions:
            objects = []
            stock_item = StockProduct(stock_product, **position)
            objects.append(stock_item)
            StockProduct.objects.bulk_create(objects)
        return stock_product
    
    
    def update(self, instance, validated_data):
        positions = validated_data.pop('positions', [])
        stock_product = super().update(instance, validated_data)
        for position in positions:
            objects = []
            stock_item = StockProduct(stock_product, **position)
            objects.append(stock_item)
            StockProduct.objects.update_or_create(stock=objects[0], product=objects[1], defaults={'price': 1, 'quantity': 1})
        return stock_product    








    

 


  
        







