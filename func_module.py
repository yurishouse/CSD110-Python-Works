import math


# Position arguments

# Change the function so that it does not print the volume
#  but return the result to the sender
def cylinder_volume(height, radius):
    volume = height * math.pi * radius ** 2
    return volume


# write another function that calculates the gross pay
# given the hours and rate and return
# the value to main function (caller)
# call the function in main and print the value

def calculate_gross_pay(hours, rate):
    return rate * hours
    # print("Your gross pay is {0:.2f}".format(gross_pay))
