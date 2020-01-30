"""This module executes an ETL for Calculated tables.
Eventually this should get promoted to a Jenkins or Apache Airflow job."""
from crontab import CronTab

# Create cron user, assumes current user
cron_user = CronTab(user=True)

# remove all jobs for current user
cron_user.remove_all()
cron_user.write()

for job in cron_user:
    print(job)
