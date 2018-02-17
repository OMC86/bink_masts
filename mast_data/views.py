from django.shortcuts import render, redirect
from django.db.models import Sum, Count
from .models import Masts
from .forms import NewMastForm
# Create your views here.


def lease_list(request):
    """
    Returns a query set ordered by current rent in ascending order
    """
    leaselist = Masts.objects.all().order_by('current_rent')
    return render(request, 'lease_list.html', {'leaselist': leaselist})


def lease_total(request):
    """
     Returns the sum of current rent column
    """
    leaselist = Masts.objects.all().order_by('current_rent')
    total = leaselist.aggregate(Sum('current_rent'))['current_rent__sum'] or 0
    return render(request, 'total.html', {'total': total})


def lease_table(request):
    """
    Returns a table in ascending order, ordered by current_rent.
      Creates a dictionary of tenant name and number of masts they're leasing from a query set that gets the tenant name
      and counts how often that name occurs.
    """
    table = Masts.objects.all().order_by('current_rent')[:5]
    names_and_frequency = Masts.objects.values('tenant_name').annotate(frequency=Count('tenant_name'))
    naf_dict = {d['tenant_name']: d['frequency'] for d in names_and_frequency}
    return render(request, 'lease_table.html', {'table': table, 'naf_dict': naf_dict})


def lease_table_d(request):
    """
    Returns a table in descending order, ordered by current_rent.
      Creates a dictionary of tenant name and number of masts they're leasing from a query set that gets the tenant name
      and counts how often that name occurs.
    """
    table = Masts.objects.all().order_by('-current_rent')[:5]
    names_and_frequency = Masts.objects.values('tenant_name').annotate(frequency=Count('tenant_name'))
    naf_dict = {d['tenant_name']: d['frequency'] for d in names_and_frequency}
    return render(request, 'lease_table.html', {'table': table, 'naf_dict': naf_dict})


def new_entry(request):
    """
    Allows the user to add a new entry to the data set
    """
    if request.method == "POST":
        form = NewMastForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(lease_list)
    else:
        form = NewMastForm()
    return render(request, 'mast_form.html', {'form': form})
