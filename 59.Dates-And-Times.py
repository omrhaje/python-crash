# Python Date / time

import datetime

date = datetime.date(2021, 8, 28)
today = datetime.date.today()

time = datetime.time(16,34,23)
now = datetime.datetime.now()

now = now.strftime("%H:%M:%S %d-%m-%Y")

target_datetime = datetime.datetime(2020, 1, 2, 12, 59, 59)
current_datetime = datetime.datetime.now()

if target_datetime < current_datetime:
    print("Target date has passed!")
else:
    print("Target date has not been passed!")