from django.db import models
from django.db.models import Sum


class Masts(models.Model):

    class Meta:
        app_label = "mast_data"

    property_name = models.CharField(max_length=100)
    property_address_1 = models.CharField(max_length=100)
    property_address_2 = models.CharField(max_length=100, blank=True)
    property_address_3 = models.CharField(max_length=100, blank=True)
    property_address_4 = models.CharField(max_length=100, blank=True)
    unit_name = models.CharField(max_length=100)
    tenant_name = models.CharField(max_length=100)
    lease_start_date = models.CharField(max_length=100)
    lease_end_date = models.CharField(max_length=100)
    lease_years = models.IntegerField(default=0)
    current_rent = models.DecimalField(max_digits=7, decimal_places=2)

    def total_rent(self):
        return Masts.objects.aggregate(Sum('current_rent'))


    def __unicode__(self):
        return self.property_name
