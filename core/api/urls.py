from django.urls import path
from .views import CourierList, MissionList, MyMissionList

app_name = 'api-v1'

urlpatterns = [
    path('couriers/', CourierList.as_view(), name='courier-list'),
    path('missions/', MissionList.as_view(), name='mission-list'),
    path('my-missions/', MyMissionList.as_view(), name='my-missions'),
]