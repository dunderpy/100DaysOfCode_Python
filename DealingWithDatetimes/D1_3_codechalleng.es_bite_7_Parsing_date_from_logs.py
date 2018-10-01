from datetime import datetime
from datetime import timedelta

logfile = "D:\\Development Projects\\100DaysOfCode_Python\\DealingWithDatetimes\\logfile.txt"

with open(logfile) as f:
    loglines = f.readlines()

print(loglines)

shutdown_time_list = []
for line in loglines:
    if 'Shutdown initiated' in line:
        print(line)
        datetime_stamp = line.split(sep=' ')[1]
        datetime_var = datetime.strptime(datetime_stamp, '%Y-%m-%dT%H:%M:%S')
        shutdown_time_list.append(datetime_var)


print(shutdown_time_list)
time_delta_var = shutdown_time_list[1] - shutdown_time_list[0]
print(time_delta_var)
print(type(time_delta_var))