from django.contrib import admin
from django.urls import path, include
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Maria Health API')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('payment_terms/', include('payment_terms.urls')),
    path('hmos/', include('hmos.urls')),
    path('plans/', include('plans.urls')),
    path('products/', include('products.urls')),
    path('order_products/', include('order_products.urls')),
    path('carts/', include('carts.urls')),
    path('', schema_view),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
