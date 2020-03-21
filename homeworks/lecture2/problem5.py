import datetime
import time
import calendar
my_birth = datetime.datetime(2020, 3, 16)
tday = datetime.datetime.today()
print('my birthday:', my_birth)
print("year:", my_birth.year)
print('month:', my_birth.month)
print('day:', my_birth.day)
print('weekday:', my_birth.weekday())
print('days till my birthday:', my_birth - tday)

cal = calendar.month(2017, 5)
print('Calendar of May', cal)
tdelta = datetime.timedelta(days = 1)
y_day = (tday - tdelta)
tdelta2 = datetime.timedelta(days = 2)
tdelta3 = datetime.timedelta(days = 3)
print('Yesterday:', y_day)
print("+ 2 days:", y_day + tdelta2)
print("- 3 days:", y_day - tdelta3)
