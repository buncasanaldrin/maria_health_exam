from django.urls import path
from .apiviews import HmoList, HmoDetail

urlpatterns = [
    path('', HmoList.as_view(), name='hmos_list'),
    path('<int:pk>/', HmoDetail.as_view(), name='hmos_detail'),
]