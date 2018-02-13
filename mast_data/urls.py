from django.conf.urls import url
from mast_data import views

urlpatterns = [
    url(r'^list/$', views.lease_list),
    url(r'^table/$', views.lease_table, name='ascending'),
    url(r'^tabled/$', views.lease_table_d, name='descending'),

]
