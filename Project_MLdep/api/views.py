from unicodedata import name
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status, generics
from .models import order
import json
import pandas as pd


class OrderView(APIView):
    
    #@method_decorator(csrf_exempt)
    #def dispatch(self, request, *args, **kwargs):
    #    return super().dispatch(request, *args, **kwargs)

    def get(self, request, order_id=0):
        if order_id > 0:
            orders = list(order.objects.filter(order_id=order_id).values())
            if len(orders)>0:
                data = {'message': 'Success', 'orders': orders[0]}
            else:
                data = {'message': 'No orders found'}
        else:    
            orders = list(order.objects.values())
            if len(orders)>0:
                data = {'message': 'Success', 'orders': orders}
            else:
                data = {'message': 'No orders found'}
        return JsonResponse(data)

    def post(self, request):
        jd = json.loads(request.body)
        df = pd.json_normalize(jd['orders'])
        print(df)
        #for i in jd['orders']:
        #    if len(list(order.objects.filter(order_id=i['order_id']).values()))==0:
        #        order.objects.create(order_id=i['order_id'],store_id=i['store_id'],
        #        to_user_distance=i['to_user_distance'],to_user_elevation=i['to_user_elevation'],
        #        total_earning=i['total_earning'],created_at=i['created_at'],taken=i['taken'])
        data = {'message': 'Success'}
        return JsonResponse(data)
        

    def put(self, request, order_id):
        jd = json.loads(request.body)
        orders = list(order.objects.filter(order_id=order_id).values())
        if len(orders)>0:
            up_order = order.objects.get(order_id=order_id)
            up_order.order_id = jd['order_id']
            up_order.store_id = jd['store_id']
            up_order.to_user_distance = jd['to_user_distance']
            up_order.to_user_elevation = jd['to_user_elevation']
            up_order.total_earning = jd['total_earning']
            up_order.created_at = jd['created_at']
            up_order.taken = jd['taken']
            up_order.save()
            data = {'message': 'Success'}
        else:
            data = {'message': 'No orders found'}
        return JsonResponse(data)

    def delete(self, request, order_id):
        orders = list(order.objects.filter(order_id=order_id).values())
        if len(orders)>0:
            order.objects.get(order_id=order_id).delete()
            data = {'message': 'Success'}
        else:
            data = {'message': 'No orders found'}
        return JsonResponse(data)
