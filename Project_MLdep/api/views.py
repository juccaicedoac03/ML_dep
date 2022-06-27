from django.http import JsonResponse
from rest_framework.views import APIView
from .models import order
import json
import pandas as pd
from ML_dep.Utils import timeConverter
from .apps import RandomForestClassifier


class OrderView(APIView):

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

        col_names = list(df.keys())
        feat_names = col_names[1::]
        prep = timeConverter(feat_names=feat_names)
        X = prep.fit_transform(df)
        #y_pred = RandomForestClassifier.mdl.predict(X)

        #for i, row in df.iterrows():
        #    if len(list(order.objects.filter(order_id=row['order_id']).values()))==0:
        #        order.objects.create(order_id=row['order_id'],store_id=row['store_id'],
        #        to_user_distance=row['to_user_distance'],to_user_elevation=row['to_user_elevation'],
        #        total_earning=row['total_earning'],created_at=row['created_at'],taken=y_pred[i])
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
