from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Item, Products
from .serializers import ItemSerializer, ProductSrializer
from django.db.models import Q


def detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    context = {
        'item': item
    }
    return render(request, 'item/detail.html', context)


@api_view()
def example(request):
    query_set = Item.objects.all()
    serializer = ItemSerializer(query_set, many=True)
    return Response(serializer.data)

@api_view()
def detailed(request, id):
    item = get_object_or_404(Item, pk=id)
    serializer = ItemSerializer(item)
    return Response(serializer.data)

@api_view()
def product_view(request):
    products = Products.objects.filter(Q(price__gt=100) & Q(price__lt=200))
    serializer = ProductSrializer(products, many=True) 
    return Response(serializer.data) 



 

