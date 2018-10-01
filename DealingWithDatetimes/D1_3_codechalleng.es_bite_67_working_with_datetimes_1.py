from datetime import date, timedelta

start_100days = date(2017, 3, 30)
pybites_founded = date(2016, 12, 19)
pycon_date = date(2018, 5, 8)


def get_hundred_days_end_date():
    """Return a string of yyyy-mm-dd"""
    eta = timedelta(days=100)
    req_date = start_100days + eta
    return str(req_date)


def get_days_between_pb_start_first_joint_pycon():
    """Return the int number of days"""
    days_diff = pycon_date - pybites_founded
    return str(days_diff.days)
    pass


print((get_hundred_days_end_date()))

print((get_days_between_pb_start_first_joint_pycon()))
