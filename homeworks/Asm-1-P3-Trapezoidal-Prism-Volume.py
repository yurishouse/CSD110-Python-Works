# Created by Zhongli Liang

# Ask user to enter Length, Height, Base Width, and Top Width values, store them in variables.

# length
length = eval(input("Enter the Length of the Trapezoidal Prism: "))
# height
height = eval(input("Enter the Height of the Trapezoidal Prism: "))
# base width
bWidth = eval(input("Enter the Base Width of the Trapezoidal Prism: "))
# top width
tWidth = eval(input("Enter the Top Width of the Trapezoidal Prism: "))

# The formula is volume = length * height * ((bWidth + tWidth)/2)
# Creates volume variable and store the final value in it.
volume = length * height * ((bWidth + tWidth) / 2)

# Print out the final volume
print(volume, "is the volume of the Trapezoidal Prism")
# Printout the measurement
print("with a length of:", length, "a height of:", height, "a Base width of:", bWidth, "and a Top width of:", tWidth)

# Reduce all the entered measurement by 25% with * 0.75
length = length * 0.75
height = height * 0.75
bWidth = bWidth * 0.75
tWidth = tWidth * 0.75

# Changes volume variable and store the final value (reduced) in it.
volume = length * height * ((bWidth + tWidth) / 2)

# Print out the final volume (reduced)
print(volume, "is the volume of the Trapezoidal Prism reduced by 25%")
# Printout the measurement (reduced)
print("with a length of:", length, "a height of:", height, "a Base width of:", bWidth, "and a Top width of:", tWidth)