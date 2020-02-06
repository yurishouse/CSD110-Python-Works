# 1 write a function that takes a value as param, doubles the value and print it to the screen.
import math


def double_value(param):
    param = param * 2
    print(param)


def main():
    param = eval(input("input the value to be doubled: "))
    double_value(param)
    height_of_cylinder = eval(input("input the height of the cylinder: "))
    base_radius_cylinder = eval(input("input the base radius of the cylinder: "))
    cal_volume_cylinder(height_of_cylinder, base_radius_cylinder)


# 2 write a function that takes two values, height and base radius of a cylinder and calculates
# the value of the cylinder
# volume = pi * radius**2 * height
def cal_volume_cylinder(height, base):
    volume = math.pi * base ** 2 * height
    print("The volume of the cylinder is {0:.4f}".format(volume))


if __name__ == '__main__':
    main()
