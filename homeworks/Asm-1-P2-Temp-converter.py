# Made by Shiina Yuri

# Let the user input the current temp in Fahrenheit, and creates fTemp variable
fTemp = eval(input("Please input the current temperature (Fahrenheit): "))

# The formula is as follows: K = (F + 459.67) × 5/9
# here's the calculation part, also created kTemp variable

kTemp = (fTemp + 459.67)*5/9

# Printout the value stored in the kTemp variable, in this case, the Kelvin temperature

print("The Kelvin Temperature is {:.3f}".format(kTemp))

