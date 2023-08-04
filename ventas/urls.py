from django.urls import path
from .views import (
    ClienteListCreateView, ClienteRetrieveUpdateDestroyView,
    ProductoListCreateView, ProductoRetrieveUpdateDestroyView,
    VentaListCreateView, VentaRetrieveUpdateDestroyView
)

urlpatterns = [
    path('', ClienteListCreateView.as_view(), name='cliente-list-create'),
    path('clientes/', ClienteListCreateView.as_view(), name='cliente-list-create'),
    path('clientes/<int:pk>/', ClienteRetrieveUpdateDestroyView.as_view(), name='cliente-retrieve-update-destroy'),
    path('productos/', ProductoListCreateView.as_view(), name='producto-list-create'),
    path('productos/<int:pk>/', ProductoRetrieveUpdateDestroyView.as_view(), name='producto-retrieve-update-destroy'),
    path('ventas/', VentaListCreateView.as_view(), name='venta-list-create'),
    path('ventas/<int:pk>/', VentaRetrieveUpdateDestroyView.as_view(), name='venta-retrieve-update-destroy'),
]
