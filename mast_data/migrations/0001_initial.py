# Generated by Django 2.0.2 on 2018-02-13 00:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Masts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('property_name', models.CharField(max_length=100)),
                ('property_address_1', models.CharField(max_length=100)),
                ('property_address_2', models.CharField(blank=True, max_length=100)),
                ('property_address_3', models.CharField(blank=True, max_length=100)),
                ('property_address_4', models.CharField(blank=True, max_length=100)),
                ('unit_name', models.CharField(max_length=100)),
                ('tenant_name', models.CharField(max_length=100)),
                ('lease_start_date', models.CharField(max_length=100)),
                ('lease_end_date', models.CharField(max_length=100)),
                ('lease_years', models.IntegerField(default=0)),
                ('current_rent', models.DecimalField(decimal_places=2, max_digits=7)),
            ],
        ),
    ]
