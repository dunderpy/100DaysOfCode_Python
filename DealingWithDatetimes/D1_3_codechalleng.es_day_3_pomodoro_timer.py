from datetime import datetime
from datetime import timedelta
from os import system


# start_time = datetime.today()
# timer_period = timedelta(minutes=0.5)
# end_time = start_time + timer_period
#
# while datetime.today() < end_time:
#     print("Timer Running {}".format((datetime.today()).time().replace(microsecond=0)))
#     system('cls')
# else:
#     print("Stop {}".format((datetime.today()).time().replace(microsecond=0)))
#     print("Start Time {}".format(start_time.time().replace(microsecond=0)))
#     print("Timer Period {}".format(timer_period))
#     print("End Time {}".format(end_time.time().replace(microsecond=0)))

def timer_app(timer_value):
    start_time = datetime.today()
    timer_period = timedelta(minutes=timer_value)
    end_time = start_time + timer_period

    while datetime.today() < end_time:
        print("Timer Running {}".format((datetime.today()).time().replace(microsecond=0)))
        system('cls')
    else:
        print("Stop {}".format((datetime.today()).time().replace(microsecond=0)))
        print("Start Time {}".format(start_time.time().replace(microsecond=0)))
        print("Timer Period {}".format(timer_period))
        print("End Time {}".format(end_time.time().replace(microsecond=0)))


BREAK_FLAG = False
pomodoro_sprint_counter = 0
pomodoro_break_counter = 0

if __name__ == '__main__':
    user_sprint_break = int(input("How many Pomodoro Sprints ? "))
    user_start_req = input("Please enter 'pomo' to start: ")
    while user_start_req.lower() == 'pomo' and pomodoro_sprint_counter <= user_sprint_break :
        if BREAK_FLAG is False:
            timer_app(1)
            BREAK_FLAG = True
            pomodoro_sprint_counter += 1
            print("Sprint Count {}".format(pomodoro_sprint_counter))
            if pomodoro_sprint_counter == 2:
                break;
        elif BREAK_FLAG is True:
            timer_app(0.5)
            BREAK_FLAG = False
            pomodoro_break_counter += 1
            print("Break Count {}".format(pomodoro_break_counter))




