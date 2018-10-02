from datetime import datetime
from datetime import timedelta
from os import system, name


start_time = datetime.today()
timer_period = timedelta(minutes=0.5)
end_time = start_time + timer_period

while datetime.today() < end_time:
    print("Timer Running {}".format((datetime.today()).time().replace(microsecond=0)))
    system('cls')
else:
    print("Stop {}".format((datetime.today()).time().replace(microsecond=0)))
    print("Start Time {}".format(start_time.time().replace(microsecond=0)))
    print("Timer Period {}".format(timer_period))
    print("End Time {}".format(end_time.time().replace(microsecond=0)))

