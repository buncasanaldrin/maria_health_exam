from django.urls import path
from .apiviews import PlanList, PlanDetail

urlpatterns = [
    path('', PlanList.as_view(), name='plans_list'),
    path('<int:pk>/', PlanDetail.as_view(), name='plans_detail'),
]