import time

my_time = int(input("Enter the time in seconds: "))

for x in range (my_time, 0, -1):
    seconds = x % 60
    Minutes = int(x / 60) % 60
    Hours = int(x / 3600)
    print(f"{Hours:02}:{Minutes:02}:{seconds:02}")
    time.sleep(1)

print("TIME'S UP!")