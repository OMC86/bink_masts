# Benchmark Test

## Getting the code up and running
1. Firstly clone this repository by running ```git clone https://github.com/OMC86/bink_masts``` command.
2. After that install dependencies listed in the requirements file.
3. To load the CSV file into the sqlite database that comes with Django:
    1. Navigate to the project root directory and run ```python manage.py shell``` from your command line.
    2. ```
          >>>import csv
          >>>from mast_data.models import masts
          >>>with open('Mobile_Phone_Masts.csv') as csvfile: 
          >>>reader = csv.DictReader(csvfile)
          >>>for row in reader:
          ...  m = Masts(property_name=row['Property Name'], property_address_1=row['Property Address One'], property_address_2=row['Property Address Two'], property_address_3=row['Property Address Three'], property_address_4=row['Property Address Four'], unit_name=row['Unit Name'], tenant_name=row['Tenant Name'], lease_start_date=row['Lease Start Date'], lease_end_date=row['Lease End Date'], lease_years=row['Lease Years'], current_rent=row['Current Rent'])
          ...  m.save()
          ...
          ...
          >>>exit()
        ```
    
    