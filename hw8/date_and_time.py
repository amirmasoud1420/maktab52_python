import datetime

date_time1 = datetime.datetime.fromisoformat(input('Enter first date-time (YYYY/MM/DD|hh:mm:ss) : '))
date_time2 = datetime.datetime.fromisoformat(input('Enter second date-time (YYYY/MM/DD|hh:mm:ss) : '))
print(date_time1, date_time2, sep='\n')
if date_time2 >= date_time1:
    difference = date_time2 - date_time1
else:
    difference = date_time1 - date_time2
print(difference.total_seconds())

