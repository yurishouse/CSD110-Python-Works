# Created by Zhongli Liang
from matplotlib.pyplot import *  # import the graph function of the matplotlib


def index_cold_day(o_temp, day):  # define the function to index the cold day and the lowest Temperature
    coldest = min(o_temp)  # find the coldest temp in the list using min function, store it in 'coldest' variable
    c_day_num = o_temp.index(coldest)  # index the location of the temperature in the original list
    c_day = day[c_day_num]  # index the coldest day using the location above
    return c_day, coldest  # return both the day and the temp


def index_warm_day(o_temp, day):  # define the function to index the warm day and the highest Temperature
    warmest = max(o_temp)  # find the warmest day using max function, then store it in the warmest variable
    w_day_num = o_temp.index(warmest)  # index the location of the temperature in the original list
    w_day = day[w_day_num]  # index the warmest day using the location above
    return w_day, warmest  # return both the day and the temp


def main():  # Define main function
    days = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']  # Set the days list with the days in a week
    temps = []  # Create empty temps list
    for day in days:  # Using a for loop to ask the user to input the temps for each day.
        info = eval(input("Enter the temperature for {0:}: ".format(day)))  # Ask user to enter the temp for the day
        # creates info variable
        temps.append(info)  # add the info to the temps list
    c_day, cold_temp = index_cold_day(temps, days)  # call for the index_cold_day function and store the two return
    # variables into local variables c_day, cold_temp
    w_day, warm_temp = index_warm_day(temps, days)  # call for the index_warm_day function and store the two return
    # variables into local variables w_day, warm_temp
    print(" {0:} was the coldest day with a temperature value of {1:}".format(c_day, cold_temp))  # Print the message
    # using c_day, cold_temp
    print(" {0:} was the warmest day with a temperature value of {1:}".format(w_day, warm_temp))  # print the message
    # Using w_day, warm_temp

    plot(days, temps, marker="o")  # making the plot using the days for x-axis and temps for y-axis, this also
    # automatically makes the x-tick the days of the week. marker is enabled for better clarity
    title("Weekly Temperature Data")  # add a title for the graph
    grid(True)  # grid is also enabled for better clarity
    # add a label to x/y
    xlabel("Days of the week")  # label for x-axis
    ylabel("Temperature values")  # label for y-axis
    # Show the final graph
    show()


if __name__ == '__main__':
    main()  # call the main function
