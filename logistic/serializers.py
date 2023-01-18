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
        fields = ['id' ,'address']    

    def create(self, validated_data):
        positions = validated_data.pop('positions', [])
        stock_product = super().create(validated_data)
        for position in positions:
            objects = []
            stock_item = StockProduct(stock_product, **position)
            objects.append(stock_item)
            StockProduct.objects.bulk_create(objects)
        return stock_product
     
    

 


  
        







