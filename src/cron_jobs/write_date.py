import datetime
with open('src/cron_jobs/dateInfo.txt', 'a') as outFile:
    outFile.write('\n' + str(datetime.datetime.now()))