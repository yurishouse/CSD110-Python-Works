from math import pi, sqrt  # Third option
# forth option: import math as m
# second option: from math import *
# first option: import math
x = 100


def mystery():
    y = 200
    z = 300

    print("From mystery: ", x, y, z)


def magic():

    print("From Magic: ", x)


def main():
    mystery()
    magic()

    # first option: y = math.pi * math.sqrt(x)
    y = pi * sqrt(x)  # Second / Third option

    print(y)


if __name__ == '__main__':
    main()
