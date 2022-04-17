from django.db import models

from django.utils import timezone
from django.urls import reverse


# Create your models here.
class Package(models.Model):
    location = models.CharField(max_length=50)
    pack_number = models.IntegerField(blank=False, null=False)
    description = models.CharField(max_length=250)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    start_date = models.DateField(default=timezone.now, blank=True, null=True)
    end_date = models.DateField(default=timezone.now, blank=True, null=True)
    rating = models.IntegerField(blank=False, null=False)
    weather = models.CharField(max_length=50)

    def created(self):
        self.recent_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.location)

    def get_absolute_url(self):
        return reverse("product", args=[str(self.id)])
