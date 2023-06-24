from django.urls import path
from .views import CourierList

urlpatterns = [
    path('couriers/', CourierList.as_view(), name='courier-list'),
]