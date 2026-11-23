from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_items, name='lista_items'),
    path('item/<int:item_id>/', views.detalle_item, name='detalle_item'),
]