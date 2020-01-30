import time

n = eval(input("Input the number per lines: "))
m = eval(input("Input the number of stars per line: "))
o = 0

for Line in range(1, n + 1):
    # print stars in one line
    for column in range(1, m + 1):
        print("{0:3d}".format(Line * column), end=' ')
    print()  # Go to next line

