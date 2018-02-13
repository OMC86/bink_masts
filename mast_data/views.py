from django.shortcuts import render, redirect, get_object_or_404
from .models import Masts
# Create your views here.


def lease_list(request):
    leaselist = Masts.objects.all().order_by('current_rent')
    return render(request, 'lease_list.html', {'leaselist': leaselist})


def lease_table(request):
    table = Masts.objects.all().order_by('current_rent')[:5]
    return render(request, 'lease_table.html', {'table': table})


def lease_table_d(request):
    table = Masts.objects.all().order_by('-current_rent')[:5]
    return render(request, 'lease_table.html', {'table': table})

