from django.contrib import admin
from .models import *


class StockProductInline(admin.TabularInline):
    model = StockProduct
  


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'description']

@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    list_display = ['address']
    inlines = [StockProductInline,]
    
    
