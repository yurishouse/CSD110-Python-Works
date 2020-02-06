# Made by Zhongli Liang
# Assignment 4
# 2/6/2020


def fr_converter(tf):  # define the fr_converter function, receive tf (temp in Fahrenheit) from main
    return (tf - 32) * (4/9)  # return the converted Réaumur temp value after calculation


def main():  # main function
    tf = eval(input("Input the temp in Fahrenheit: "))  # ask the user to input the temp in Fahrenheit
    # creates tf variable
    print("The temp is {0:.2f} in Réaumur".format(fr_converter(tf)))
    # call for the fr_converter function and given variable tf -> tf
    # then print the returned result.


if __name__ == '__main__':
    main()  # call for main function
