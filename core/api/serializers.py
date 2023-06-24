from accounts.models import Courier
from rest_framework import serializers

class CourierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Courier
        fields = ('pk', 'phone', 'longitude', 'latitude', 'password')