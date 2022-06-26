# Generated by Django 4.0.5 on 2022-06-26 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='orders',
            fields=[
                ('order_id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('store_id', models.BigIntegerField(max_length=10)),
                ('to_user_distance', models.FloatField(max_length=200)),
                ('to_user_elevation', models.FloatField(max_length=200)),
                ('total_earning', models.BigIntegerField(max_length=10)),
                ('created_at', models.TextField(max_length=25)),
                ('taken', models.BooleanField()),
            ],
        ),
    ]
