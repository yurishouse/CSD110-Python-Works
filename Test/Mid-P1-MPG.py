# Made by Shiina Yuri


def calculate_mpg(miles, gallon):  # Create function calculate_mpg with the formula
    return miles / gallon  # MPG = Miles driven / Gallons of gas used


def main():  # Create main function
    mile = eval(input("Please input the miles you've driven: "))  # ask user to input the miles
    gal = eval(input("Please input the gallons of gas used: "))  # ask the user to input gallon of gas used
    print("the car runs at {0:.3f} miles per gallon".format(calculate_mpg(mile, gal)))  # Call for calculate_mpg and print out the
    # return value


if __name__ == '__main__':
    main()  # Call for main

