import datetime
import time
from datetime import timedelta
tday = datetime.datetime.today()
tdelta = datetime.timedelta(days = 5)
after = tday + tdelta
before = tday - tdelta
print(tday)
print(tday.year)
print(tday.month)
print(tday.weekday())
print(after)
print(before)