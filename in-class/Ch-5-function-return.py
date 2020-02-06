import math


# Position arguments

# Change the function so that it does not print the volume
#  but return the result to the sender
def cylinder_volume(height, radius):
    volume = height * math.pi * radius ** 2
    return volume


def main():  # Scope of the main program logic
    h = 300
    r = 20
    vol = cylinder_volume(h, r)
    # Using position arguments
    # cylinder_volume(radius=r, height=h)
    print("volume is {0:.3f}".format(vol))

    print("Another volume {0:.3f}".format(cylinder_volume(23, 55)))

    hours_worked = eval(input("hours worked: "))
    pay_rate = eval(input("Your pay rate: "))
    print("Your gross pay is: {0:.2f}".format(calculate_gross_pay(hours_worked, pay_rate)))


# write another function that calculates the gross pay
# given the hours and rate and return
# the value to main function (caller)
# call the function in main and print the value

def calculate_gross_pay(hours, rate):
    gross_pay = rate * hours
    return gross_pay
    # print("Your gross pay is {0:.2f}".format(gross_pay))


if __name__ == '__main__':
    main()
