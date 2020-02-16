# Made by Zhongli Liang

mile = eval(input("Please input the miles you've driven: "))  # ask user to input the miles
gal = eval(input("Please input the gallons of gas used: "))  # ask the user to input gallon of gas used

mpg = mile / gal  # MPG = Miles driven / Gallons of gas used

print("the car runs at {0:.3f} miles per gallon".format(mpg))  # print out the result
