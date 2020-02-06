# Made by Zhongli Liang
# Assignment 4
# 2/6/2020
from math import pi  # only import pi from math library


def cone_volume(height, radius):  # define the cone_volume function, receive height and radius from main.
    return (1 / 3 * pi) * (radius ** 2) * height  # return the value after calculating it with the formula


def main():  # define main function
    h = eval(input("input the height of the cone: "))  # Ask the user to input the height of the cone
    # create h variable
    r = eval(input("input the radius of the cone: "))  # Ask the user to input the radius of the cone
    # create r variable
    print("The volume of the cone is {0:.4f}".format(cone_volume(height=h, radius=r)))
    # call for the cone_volume function and given variable height = h and radius = r
    # then print the returned result.


if __name__ == '__main__':
    main()  # call for main function
