
import datetime

date = datetime.date(2025,9, 3)
today = datetime.date.today()

time = datetime.time(14, 27,0)
now = datetime.datetime.now()

now = now.strftime("%H:%M:%S  %d-%m-%Y")

# print(now)

target_datetime = datetime.datetime(2025,9,1, 15,0,0)
current_datetime = datetime.datetime.now()

while True:
    #^^ was made for fun, and it can also eat CPU performance

    if target_datetime < current_datetime:
        print("Arrived to the target time")
        break
    else:
        print("Still on the way to the target time")
        continue