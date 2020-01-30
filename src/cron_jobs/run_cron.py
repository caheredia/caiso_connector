"""This module executes an ETL for Calculated tables.
Eventually this should get promoted to a Jenkins or Apache Airflow job."""
from os import getcwd
from crontab import CronTab

current_directory = getcwd()
relative_file_location = "src.cron_jobs.write_date"
# Create cron user, assumes current user
cron_user = CronTab(user=True)

# Create cron jobs
job = cron_user.new(
    command=f"cd {current_directory} && python3 -m {relative_file_location}",
    comment='Initial Cron job')


# Schedule job
job.minute.every(1)

# write jobs
#cron_user.remove_all()
cron_user.write()

for job in cron_user:
    print(job)

# python3 ~/Documents/2019/database-api/src/accumulo/views/hello.py >> ~/Documents/2019/database-api/src/accumulo/views/a.txt 2>&1
