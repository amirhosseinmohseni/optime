from django.db import models
from accounts.models import Courier
from django.utils import timezone


class Mission(models.Model):
    """
        Mission model is the model of mission and assign to an available courier
    """
    courier = models.ForeignKey(Courier, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=255)
    origin_latitude = models.DecimalField(max_digits=9, decimal_places=6)
    origin_longitude = models.DecimalField(max_digits=9, decimal_places=6)
    is_get = models.BooleanField(default=False)
    start_time = models.DateTimeField(null=True, blank=True)
    destination_latitude = models.DecimalField(max_digits=9, decimal_places=6)
    destination_longitude = models.DecimalField(max_digits=9, decimal_places=6)
    done = models.BooleanField(default=False)
    done_time = models.DateTimeField(null=True, blank=True)
    
    def __str__(self):
        return self.name
    
    """
        set start time and done time automatically when boolean fields get filled
    """
    def save(self, *args, **kwargs):
        if self.courier_id and not self.start_time:
            self.start_time = timezone.now()
            self.courier.is_available = False
            self.is_get = True
            self.courier.save()
        if self.done and not self.done_time:
            self.done_time = timezone.now()
            self.courier.is_available = True
            self.courier.save()
        if not self.courier:
            pass    
        super().save(*args, **kwargs)