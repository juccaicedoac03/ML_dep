# Generated by Django 4.0.5 on 2022-06-28 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='order',
            fields=[
                ('order_id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('store_id', models.BigIntegerField()),
                ('to_user_distance', models.FloatField(max_length=200)),
                ('to_user_elevation', models.FloatField(max_length=200)),
                ('total_earning', models.BigIntegerField()),
                ('created_at', models.TextField(max_length=25)),
                ('taken', models.BooleanField()),
            ],
        ),
    ]
