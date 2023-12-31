# Generated by Django 4.2.6 on 2023-10-19 13:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('customer_app', '0001_initial'),
        ('driver_app', '0001_initial'),
        ('payment_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('delivery_address', models.TextField()),
                ('order_items', models.TextField()),
                ('total_price', models.BigIntegerField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer_app.customer')),
                ('driver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='driver_app.driver')),
                ('payment_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='payment_app.payment')),
                ('status', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='order_app.orderstatus')),
            ],
        ),
    ]
