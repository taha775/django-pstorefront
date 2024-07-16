from django.shortcuts import render
from django.http import HttpResponse
from django.db.models.aggregates import Min, Max, Count, Sum, Avg
from django.db.models import Q, F, ExpressionWrapper, DecimalField
from store.models import Product, Customer, Collection, Order, OrderItem
from tags.models import TaggedItems
from django.db import transaction
from django.contrib.contenttypes.models import ContentType

def say_hello(request):
   # ....
   

   return render(request, "hello.html", {'name': "taha"})
