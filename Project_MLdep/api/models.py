from django.db import models

class orders(models.Model):
    order_id = models.BigIntegerField(primary_key=True,max_length=10)
    store_id = models.BigIntegerField(max_length=10)
    to_user_distance = models.FloatField(max_length=200)
    to_user_elevation = models.FloatField(max_length=200)
    total_earning = models.BigIntegerField(max_length=10)
    created_at = models.TextField(max_length=25)
    taken = models.BooleanField()