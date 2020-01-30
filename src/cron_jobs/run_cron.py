"""This module executes an ETL for Calculated tables.
Eventually this should get promoted to a Jenkins or Apache Airflow job."""
from os import getcwd
import subprocess
from crontab import CronTab

current_directory = getcwd()
relative_file_location = "src.cron_jobs.write_date"

# Create cron user, assumes current user
cron_user = CronTab(user=True)
print('Cron User: ', cron_user)

# Create cron jobs
out = subprocess.Popen(["which", "python3"], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
python_path = out.communicate()[0].decode().strip()

job = cron_user.new(
    command=f"cd {current_directory} && {python_path} -m {relative_file_location}",
    comment='Initial Cron job')

# Schedule job
job.minute.every(1)

# write jobs
cron_user.write()

for job in cron_user:
    print(job)

# python3 ~/Documents/2019/database-api/src/accumulo/views/hello.py >> ~/Documents/2019/database-api/src/accumulo/views/a.txt 2>&1
