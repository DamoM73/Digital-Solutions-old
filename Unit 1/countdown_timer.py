import time

time_remaining = 90

while time_remaining > 0:
    minutes = str(time_remaining // 60)
    seconds = time_remaining % 60
    if seconds < 10:
        seconds = "0"+str(seconds)
    else:
        seconds = str(seconds)
    print(minutes+":"+seconds)
    time_remaining -= 1
    time.sleep(1)

    