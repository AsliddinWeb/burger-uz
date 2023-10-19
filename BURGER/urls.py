from django.contrib import admin
from django.urls import path, include

admin.site.site_header = 'BurgerUz Dashboard'                    # default: "Django Administration"
admin.site.index_title = 'Hi Admin!'                 # default: "Site administration"
admin.site.site_title = 'BurgerUz' # default: "Django site admin"

# Static settings
from django.conf import settings
from django.conf.urls.static import static

# DRF Yasg
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

schema_view = get_schema_view(
   openapi.Info(
      title="BurgerUz API",
      default_version='v1',
      description="Super XotDog",
   ),
public=True,
    permission_classes=(permissions.AllowAny,),
)



urlpatterns = [
    path('admin/', admin.site.urls),

    # API
    path('api/v1/customer/', include('customer_app.urls')),
    path('api/v1/menu/', include('menu_app.urls')),
    path('api/v1/payment/', include('payment_app.urls')),
    path('api/v1/order/', include('order_app.urls')),

    # Swagger
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
              + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
