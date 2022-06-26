from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status, generics
from .models import order

class OrderView(View):

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
