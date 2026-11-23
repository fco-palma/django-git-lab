from django.urls import path
from . import views

urlpatterns = [
    path('agregar/<int:item_id>/', views.agregar_resena, name='agregar_resena'),
]