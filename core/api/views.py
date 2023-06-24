from django.shortcuts import render
from accounts.models import User, Courier
from rest_framework import generics
from .serializers import CourierSerializer
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from django.contrib.auth.hashers import make_password


class CourierList(generics.ListCreateAPIView):
    queryset = Courier.objects.all()
    serializer_class = CourierSerializer
    permission_classes = [IsAdminUser]
    
    def get(self, request):
        queryset = Courier.objects.all()
        serializer = CourierSerializer(queryset, many=True)
        return Response(serializer.data)
    def perform_create(self, serializer):
        password = serializer.validated_data.get('password')
        hashed_password = make_password(password)
        serializer.save(password=hashed_password)