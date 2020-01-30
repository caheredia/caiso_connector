import datetime
with open('src/cron_jobs/date_info.txt', 'a') as outFile:
    outFile.write('\n' + datetime.datetime.now().isoformat())