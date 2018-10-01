from datetime import datetime
from datetime import date

today = datetime.today()
print("Today".center(25, "*"))
print(today)
print(type(today))
print(30 * '*')

todaydate = date.today()
print("todaydate".center(25, "*"))
print(todaydate)
print(type(todaydate))
print(30 * '*')

christmas = date(2018, 12, 18)
print("christmas".center(25, "*"))
print(christmas)

days_to_xmas = christmas - todaydate

print((days_to_xmas).days)
print(type((days_to_xmas)))

if christmas is not todaydate:
    print("{} days to xmas!".format((christmas - todaydate).days))
else:
    print("Merry Xmas!")


print(30 * '*')