# real_time_dashboard
Django 3.0.8
Import data from .csv into SQLite db
Displays data by time (bootstrap css and some js files) 
Uses computer time as time, see date in spreadsheet. 
Can manually set time to be displayed: http://127.0.0.1:8000/t=08:00:32 

pip3 install django
python3 manage.py migrate
python3 manage.py load_dashboard_data
