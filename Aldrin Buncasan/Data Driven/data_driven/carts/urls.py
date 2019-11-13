from django.urls import path
from .apiviews import CartDetail

urlpatterns = [
    path('<int:pk>/', CartDetail.as_view(), name='carts_detail'),
]