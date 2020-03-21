import datetime
from datetime import timedelta
num_y = int(input('insert the number of years: '))
num_d = int(input('insert the number of days: '))
tday = datetime.datetime.today()
tdelta = datetime.timedelta( days = (num_y * 365) + num_d)
print("Current Date: ", tday)
print('Given years: ', num_y)
print('Given days: ', num_d)
print('Final Date: ', tday - tdelta)
