# Benchmark Test

## Getting the code up and running
1. Firstly clone this repository by running ```git clone https://github.com/OMC86/bink_masts``` command.
2. After that, install dependencies listed in requirements.txt.
3. To create the table and load the CSV file into the database that comes shipped with Django:
    1. First, in the project root directory, run ```python manage.py migrate``` to create tables.
    2. Next run ```python manage.py shell``` from your command line and follow these steps in the python shell.
    3. ```
          >>> import csv
          >>> from mast_data.models import Masts
          >>> with open('Mobile_Phone_Masts.csv') as csvfile: 
          >>> reader = csv.DictReader(csvfile)
          >>> for row in reader:
          ...   m = Masts(property_name=row['Property Name'], property_address_1=row['Property Address One'], property_address_2=row['Property Address Two'], property_address_3=row['Property Address Three'], property_address_4=row['Property Address Four'], unit_name=row['Unit Name'], tenant_name=row['Tenant Name'], lease_start_date=row['Lease Start Date'], lease_end_date=row['Lease End Date'], lease_years=row['Lease Years'], current_rent=row['Current Rent'])
          ...   m.save()
          ...
          ...
          >>> exit()
        ```
## Problems that Arose
- A lot of the tenant names had typos. I used Pandas to clean the data in order to make query results more accurate when displaying the mast count for each tenant. For that reason please load in the CSV file provided in this repository as opposed to the original.