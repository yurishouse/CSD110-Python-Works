# Made by Shiina Yuri

mass = eval(input("Please input the mass of the object in kilograms: "))  # ask the user to input the mass

newton = mass * 9.8  # calculate weight with formula: weight = mass x 9.8

print("the weight of the object is {0:.3f} newton".format(newton))  # Print out the weight in newton

# Compare the value, If the object weighs more than 100 newtons, indicating that it is too heavy.
# If the object weighs less than 10 newtons, indicating that it is too light. Otherwise,
# display a message indicating that its weight is normal.
if newton > 100:
    print("It's too heavy")
elif newton < 10:
    print("It's too light")
else:
    print("the weight is normal")

