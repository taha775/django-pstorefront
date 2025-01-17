from typing import Any
from django.contrib import admin
from django.db.models.query import QuerySet
from django.db.models.aggregates import Count
from django.http import HttpRequest
from . import models
# Register your models here.



@admin.register(models.Product)

class ProductAdmin(admin.ModelAdmin):
    list_display =['title','unit_price','inventory_status','collection']
    list_editable =['unit_price']
    list_per_page = 10 
    list_select_related = ['collection']


    # def collection_title(self,product):
    #     return product.collection.title
    

    @admin.display(ordering='inventory')
    def inventory_status(slef,product):
        if product.inventory < 10:    #  its identiyfing the attribute from product class only work if attribute exits in that class
            return 'Low'
        return 'ok'

@admin.register(models.Customer)

class CustomerAdmin(admin.ModelAdmin):
    list_display =['first_name','last_name','membership']
    list_editable =['membership']
    ordering =['first_name','last_name']
    list_per_page = 10 


#collections


@admin.register(models.Collection)

class CollectionAdmin(admin.ModelAdmin):
    list_display =['title','products_count']


    @admin.display(ordering='products_count')
    def products_count(self,collection):
        return collection.products_count 
    
    def get_queryset(self, request):
        return super().get_queryset(request).annotate(
        products_count = Count('product')            
        )


# order models
@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    list_display =['id','placed_at','payment_status','customer']
    list_editable =['payment_status']

    # def customer_first_name(self,order):
    #     return order.customer.first_name  instead of using thse crete a msgic struing inthat particulr model 

 

