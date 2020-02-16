# Made by Zhongli Liang


def calculate_mass(mass):  # Create function calculate_mass with the formula
    return mass * 9.8  # weight = mass x 9.8


def main():  # Create main function
    mass = eval(input("Please input the mass of the object in kilograms: "))  # ask the user to input the mass
    newton = calculate_mass(mass)
    print("the weight of the object is {0:.3f} newton".format(newton))
    if newton > 100:
        print("It's too heavy")
    elif newton < 10:
        print("It's too light")
    else:
        print("the weight is normal")


if __name__ == '__main__':
    main()  # Call for main
