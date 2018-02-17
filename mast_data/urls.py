from django.conf.urls import url
from mast_data import views

urlpatterns = [
    url(r'^list/$', views.lease_list, name='list'),
    url(r'^total/$', views.lease_total, name='total'),
    url(r'^table/$', views.lease_table, name='ascending'),
    url(r'^tabled/$', views.lease_table_d, name='descending'),
    url(r'^form/$', views.new_entry, name='new_entry'),

]
