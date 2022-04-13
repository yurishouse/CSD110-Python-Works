# Made by Shiina Yuri
def main():
    # List of months used to create the dict
    months = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']
    # Create an empty dict
    year = {}
    # loop through months and ask user to input the rainfall value, store both into year as a key-value pair
    for month in months:
        year[month] = eval(input("Enter the total rainfall for {0:} here: ".format(month)))
    # Create a empty variable use to store the total rainfall value
    total_rainfall = 0
    # Loop through all the values in year and add them to total_rainfall
    for num in year.values():
        total_rainfall += num
    # Print out the total rainfall
    print("the total rainfall is: {0:.2f}".format(total_rainfall))
    # print out the average rainfall using sum of all the values divide by number of months
    print('The average rainfall is {0:.2f}'.format(float(sum(year.values())) / len(months)))
    # print out the lowest rainfall using min function
    print('The lowest rainfall is', min(year.values()), 'at', min(year, key=lambda x: year[x]))
    # print out the highest rainfall using max function
    print('The highest rainfall is', max(year.values()), 'at', max(year, key=lambda x: year[x]))


if __name__ == '__main__':   # Call for main function
    main()