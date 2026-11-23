from django.shortcuts import render, get_object_or_404, redirect
from catalogo.models import Item
from .models import Resena

def agregar_resena(request, item_id):
    if request.method == 'POST':
        item = get_object_or_404(Item, id=item_id)
        Resena.objects.create(
            item=item,
            autor=request.POST.get('autor'),
            puntuacion=int(request.POST.get('puntuacion')),
            comentario=request.POST.get('comentario')
        )
    return redirect('detalle_item', item_id=item_id)
