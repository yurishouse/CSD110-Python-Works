import time
# simulate a US clock

for hour in range(12):
    for minute in range(60):
        for second in range(60):
            print(hour, ":", minute, ":", second)
            time.sleep(1)
