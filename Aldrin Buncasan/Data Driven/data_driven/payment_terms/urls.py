from django.urls import path
from .apiviews import PaymentTermList, PaymentTermDetail

urlpatterns = [
    path('', PaymentTermList.as_view(), name='payment_terms_list'),
    path('<int:pk>/', PaymentTermDetail.as_view(), name='payment_terms_detail'),
]