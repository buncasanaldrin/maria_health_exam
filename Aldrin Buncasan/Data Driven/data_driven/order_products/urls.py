from django.urls import path
from .apiviews import OrderProductList, OrderProductDetail

urlpatterns = [
    path('', OrderProductList.as_view(), name='order_products_list'),
    path('<int:pk>/', OrderProductDetail.as_view(), name='order_products_detail'),
]