from django.urls import path
from .apiviews import ProductList, ProductDetail

urlpatterns = [
    path('', ProductList.as_view(), name='products_list'),
    path('<int:pk>/', ProductDetail.as_view(), name='products_detail'),
]