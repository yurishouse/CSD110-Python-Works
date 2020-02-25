# Created by Zhongli Liang
from matplotlib.pyplot import *


def cold_day(temp):
    temp.sort
    return

def main():
    days = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
    temps = {}
    for day in days:
        info = eval(input("Enter the temperature for {0:}: ".format(day)))
        temps[day] = info
    print(temps)


if __name__ == '__main__':
    main()