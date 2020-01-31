"""This module executes an ETL for Calculated tables.
Eventually this should get promoted to a Jenkins or Apache Airflow job."""
from os import getcwd
import subprocess

current_directory = getcwd()
relative_file_location = "src.cron_jobs.write_date"



# Get system python path, depends on OS
out = subprocess.Popen(["which", "python3"], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
python_path = out.communicate()[0].decode().strip()

# Create cron jobs
date_cron_frequency = "* * * * *"

date_cron = f"""
    {date_cron_frequency} cd {current_directory} && {python_path} -m {relative_file_location} # write date
    # An empty line is required at the end of this file for a valid cron file"""

print(date_cron)




# python3 ~/Documents/2019/database-api/src/accumulo/views/hello.py >> ~/Documents/2019/database-api/src/accumulo/views/a.txt 2>&1
