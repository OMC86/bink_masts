from django.forms import ModelForm
from .models import Masts
from django.utils.translation import ugettext_lazy as _


class NewMastForm(ModelForm):

    class Meta:
        model = Masts
        fields = ('property_name', 'property_address_1', 'property_address_2', 'property_address_3',
                  'property_address_4', 'unit_name', 'tenant_name', 'lease_start_date', 'lease_end_date',
                  'lease_years', 'current_rent')
