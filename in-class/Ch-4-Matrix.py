
n = eval(input("Input the number per lines: "))
m = eval(input("Input the number of stars per line: "))


for Line in range(n):
    # print stars in one line
    for column in range(m):
        print('x', end=' ')
    print()  # Go to next line

