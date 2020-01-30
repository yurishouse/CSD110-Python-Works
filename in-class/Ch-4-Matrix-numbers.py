import time

n = eval(input("Input the number per lines: "))
m = eval(input("Input the number of stars per line: "))
o = 0

for Line in range(1, n + 1):
    # print stars in one line
    for column in range(1, m + 1):
        print("{0:3d}".format(Line * column), end=' ')
    print()  # Go to next line

# simulate a US clock

for hour in range(12):
    for minute in range(60):
        for second in range(60):
            print(hour, ":", minute, ":", second)
            time.sleep(1)
