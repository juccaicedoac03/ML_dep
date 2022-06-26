from django import dispatch
from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status, generics
from .models import order

class OrderView(View):
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request): 
        orders = list(order.objects.values())
        if len(orders)>0:
            data = {'message': 'Success', 'orders': orders}
        else:
            data = {'message': 'No orders found'}
        return JsonResponse(data)

    def post(self, request):
        pass

    def put(self, request):
        pass

    def delete(self, request):
        pass
