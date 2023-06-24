from django.shortcuts import render
from accounts.models import User, Courier
from actions.models import Mission
from rest_framework import generics
from .serializers import CourierSerializer, MissionSerializer
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from django.contrib.auth.hashers import make_password
from math import radians, sin, cos, sqrt, atan2
from django.shortcuts import redirect


class CourierList(generics.ListCreateAPIView):
    """
        this view is for admin to see couriers with get method and create courier with post method 
    """
    queryset = Courier.objects.all()
    serializer_class = CourierSerializer
    permission_classes = [IsAdminUser]
    
    def get(self, request):
        queryset = Courier.objects.all()
        serializer = CourierSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def perform_create(self, serializer):
        """
            this method hash the input password
        """
        password = serializer.validated_data.get('password')
        hashed_password = make_password(password)
        serializer.save(password=hashed_password)
        
class MissionList(generics.ListCreateAPIView):
    """
        this view is for admin to see missions with get method and create mission with post method 
    """
    queryset = Mission.objects.all()
    serializer_class = MissionSerializer
    permission_classes = [IsAdminUser]
    
    def get(self, request):
        queryset = Mission.objects.all()
        serializer = MissionSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def perform_create(self, serializer):
        """
            if courier foreignkey is not in input values, this method assign a courier to mission by generate_courier method
        """
        origin_latitude = serializer.validated_data.get('origin_latitude')
        origin_longitude = serializer.validated_data.get('origin_longitude')
        if not serializer.validated_data.get('courier'):
            courier = self._generate_courier(origin_latitude, origin_longitude)
            serializer.validated_data['courier'] = courier
        serializer.save()

    def _generate_courier(self, origin_latitude, origin_longitude):
        """
            this method return courier that is nearest available courier to origin location of defined mission 
        """
        couriers = Courier.objects.filter(is_available=True)
        closest_courier = None
        closest_distance = float('inf')
        for courier in couriers:
            distance = self.haversine_distance(origin_latitude, origin_longitude, courier.latitude, courier.longitude)
            if distance < closest_distance:
                closest_courier = courier
                closest_distance = distance
        if closest_courier:
            closest_courier.is_available = False
            closest_courier.save()
            return closest_courier
    
    def haversine_distance(self, origin_latitude, origin_longitude, courier_latitude, courier_longitude):
        """
            this method is for calculate difference between 2 points by latitudes and longitude points by haversine math function
        """
        origin_latitude, origin_longitude, courier_latitude, courier_longitude = map(radians, [origin_latitude, origin_longitude, courier_latitude, courier_longitude])
        difference_latitude = courier_latitude - origin_latitude
        difference_longitude = courier_longitude - origin_longitude
        a_value = sin(difference_latitude / 2) ** 2 + cos(origin_latitude) * cos(courier_latitude) * sin(difference_longitude / 2) ** 2
        c_value = 2 * atan2(sqrt(a_value), sqrt(1 - a_value))
        radius = 6371
        distance = radius * c_value
        return distance
    
class MyMissionList(generics.ListAPIView):
    """
        this view is for courier to see his missions with get method 
    """
    queryset = Mission.objects.all()
    serializer_class = MissionSerializer
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        """
            if user that send a request is admin, redirect to all missions list and if not direct to my-mission list page
        """
        if request.user.is_superuser:
            return redirect('api-v1:mission-list')
        queryset = self.queryset.filter(courier__phone=request.user)
        serializer = MissionSerializer(queryset, many=True)
        return Response(serializer.data)