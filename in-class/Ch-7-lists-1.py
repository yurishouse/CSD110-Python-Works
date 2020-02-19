# Empty List: convention is to have the name plural

items = []

# 2nd method

item2 = list()  # List constructor

print(item2)
print(items)

family = ["Yuri", "Hinata", "Neko", "Izumi"]

print(family)

# list of characters that spell out a text

characters = list("CSD111 Python")

print(characters)

# Using a loop to iterate over a list

for item in characters:
    print(item, end='')
print()

for people in family:
    print(family)
print()

# init a list (populating a list with initial values)

# we have a list of 100 items all set to 0

values = [0] * 100

print(values)

# Concatenation of lists (combine multiple list into one list)

list1 = [15, 22, 35, 45]
list2 = [22, 155, 188, 25]
newList = list1 + list2
print(list1)
print(list2)
print(newList)

# exercise
"""
Create a list of 10 int values
and then use a loop to calculate the total value
in the list: running total
"""

numbers = [15, 23, 45, 34, 22, 66, 87, 54, 9, 10]
result = 0
for total in numbers:
    result += total
print(result)

