from django.urls import path
from .views import CourierList, MissionList

app_name = 'api-v1'

urlpatterns = [
    path('couriers/', CourierList.as_view(), name='courier-list'),
    path('missions/', MissionList.as_view(), name='mission-list'),
]