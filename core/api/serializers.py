from accounts.models import Courier
from actions.models import Mission
from rest_framework import serializers

class CourierSerializer(serializers.ModelSerializer):
    """
        this serializer is for admin to see list of all couriers 
    """
    class Meta:
        model = Courier
        fields = ('pk', 'phone', 'longitude', 'latitude', 'is_available', 'password')
        read_only_fields = ('is_available',)
        
class MissionSerializer(serializers.ModelSerializer):
    """
        this serializer is for admin to see list of missions and show available couriers 
    """
    courier = serializers.PrimaryKeyRelatedField(
        queryset=Courier.objects.filter(is_available=True)
    )
    
    class Meta:
        model = Mission
        fields = ('pk', 'courier', 'name', 'origin_latitude', 'origin_longitude', 'destination_latitude', 'destination_longitude', 'is_get', 'start_time', 'done', 'done_time')
        read_only_fields = ('is_get', 'start_time', 'done', 'done_time')