from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Item
from .serializers import ItemSerializer


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

 

