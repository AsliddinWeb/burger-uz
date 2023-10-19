from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # API
    path('api/v1/customer/', include('customer_app.urls')),
    path('api/v1/menu/', include('menu_app.urls')),
    path('api/v1/payment/', include('payment_app.urls')),
    path('api/v1/order/', include('order_app.urls')),
]
