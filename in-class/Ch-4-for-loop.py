"""
counter = 0

while counter < 10:
    print("Hello World")
    counter = counter + 1  # adding 1 to counter

"""

for i in range(10):
    print("Hello world")

# Practice
# write a loop to output the following numbers
# 10 15 20 25 30 35

for x in range(10, 36, 5):
    print(x, end=" ")

print()  # Go to next line
# 77 66 55 44 33 22 11

for y in range(77, 10, -11):
    print(y, end=" ")

print()  # Go to next line

# calculate the running total for the following numbers:
# 3 7 11 15 19 24 29

total = 0

for number in range(3, 30, 4):
    # add the current number to the total
    total = total + number
    print(number, end=" ")

print("Total =", total)

# change the loop above to have it print the following
# 3 + 7 + 11 + 15 + 19 + 24 + 29 = 105

total = 0

for number in range(3, 30, 4):
    # add the current number to the total
    total = total + number
    if number < 27:
        print(number, end=" + ")
    else:
        print(number, end=" ")
print("=", total)
