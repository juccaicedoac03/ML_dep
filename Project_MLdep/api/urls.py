from django.urls import path
from .views import OrderView

urlpatterns = [
    path('Orders/', OrderView.as_view(),name='orders_list'),
]