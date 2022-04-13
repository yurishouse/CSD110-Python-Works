# Made by Shiina Yuri

# Ask the User to input the weight
# creates weight variable
weight = eval(input("Please input the weight of your package here: "))

# compare the weight to the shipping rate

if weight <= 2:  # 2 pounds or less
    sRate = 1.10
elif weight <= 6:  # Over 2 pounds but not more than 6 pounds
    sRate = 2.20
elif weight <= 10:  # Over 6 pounds but not more than 10 pounds
    sRate = 3.70
else:
    sRate = 3.80  # Over 10 pounds

# Calculate the shipping charges (weight x shipping rate)
# create sCharge
sCharge = weight * sRate

# print the final charge to the screen

print("Package that weights", weight, "pounds will cost $ {:.2f} to ship.".format(sCharge))
