from django.shortcuts import render, get_object_or_404
from .models import Item

def lista_items(request):
    items = Item.objects.all()
    return render(request, 'catalogo/lista.html', {'items': items})

def detalle_item(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    return render(request, 'catalogo/detalle.html', {'item': item})