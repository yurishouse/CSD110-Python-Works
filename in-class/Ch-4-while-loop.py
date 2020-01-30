
"""
Syntax of a while loop

while condition:
    block of code

"""

# output a message 10 times

# without loops
"""

print("Hello world")
print("Hello world")
print("Hello world")
print("Hello world")
print("Hello world")
print("Hello world")
print("Hello world")
print("Hello world")
print("Hello world")
print("Hello world")

"""

# with a loop
"""
counter = 0

while counter < 10:
    print("Hello World")
    counter = counter + 1  # adding 1 to counter
"""
# A while loop is not determinate loop: the number of repetitions
# is controlled by condition, there's no counting

# example loop that ask the user to input a integer value and the loop
# Shall terminate if user enters a negative value

value = int(0)

while value >= 0:  # While value is positive
    value = int(input("please enters new value: "))
    if value >= 0:
        print("The value is not negative")
print("Done")

