from django.db import models

class order(models.Model):
    order_id = models.BigIntegerField(primary_key=True)
    store_id = models.BigIntegerField()
    to_user_distance = models.FloatField(max_length=200)
    to_user_elevation = models.FloatField(max_length=200)
    total_earning = models.BigIntegerField()
    created_at = models.TextField(max_length=25)
    taken = models.BooleanField()