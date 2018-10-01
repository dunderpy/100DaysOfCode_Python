from datetime import datetime
from datetime import timedelta

t = timedelta(days=4, hours=10)
print(t)
print(type(t))

print(t.days)
print(t.seconds)
print(t.seconds/60/60)

eta = timedelta(hours=6)

timedelta(0, 21600)

today = datetime.today()


print(str(today + eta))
