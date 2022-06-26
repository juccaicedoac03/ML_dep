from django.urls import path
from .views import OrderView

urlpatterns = [
    path('Orders/', OrderView.as_view(),name='orders_list'),
    path('Orders/<int:order_id>/', OrderView.as_view(),name='orders_process'),
]