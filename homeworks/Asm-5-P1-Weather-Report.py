# Created by Zhongli Liang
from matplotlib.pyplot import *  #


def index_cold_day(o_temp, day):
    temp = list(o_temp)
    coldest = min(temp)
    c_day_num = o_temp.index(coldest)
    c_day = day[c_day_num]
    return c_day, coldest


def index_warm_day(o_temp, day):
    temp = list(o_temp)
    warmest = max(temp)
    w_day_num = o_temp.index(warmest)
    w_day = day[w_day_num]
    return w_day, warmest


def main():
    days = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
    temps = []
    for day in days:
        info = eval(input("Enter the temperature for {0:}: ".format(day)))
        temps.append(info)
    o_temp = tuple(temps)
    c_day, cold_temp = index_cold_day(o_temp, days)
    w_day, warm_temp = index_warm_day(o_temp, days)
    print(" {0:} was the coldest day with a temperature value of {1:}".format(c_day, cold_temp))
    print(" {0:} was the warmest day with a temperature value of {1:}".format(w_day, warm_temp))

    plot(days, temps, marker="o")
    title("Weekly Temperature Data")
    grid(True)
    # add a label to x/y
    xlabel("Days of the week")
    ylabel("Temperature values")
    # Show the final graph
    show()


if __name__ == '__main__':
    main()
