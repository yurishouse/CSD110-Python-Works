numbers = [7, 5, 3, 4, 77, 44, 55, 64, 74]

print(numbers[:])  # everything

print(numbers[::2])  # every other element

print(numbers[1:5])  # a slice 1-4

sub_numbers = numbers[2:7]  # Create a sublist 2-6

print(sub_numbers)

# the "in" operator
# we use it in a loop to go over all elements
# we also use in if statement to check if the itemlist
# contains an item / element

item = 11

# check if item is in the numbers list

if item in numbers:
    print("Yahoo!")
else:
    print("Kahoot!")


# populate an empty list
# define an empty list
# use a loop to request values from the user
# and add it to the list
lists = []
"""
for i in range(5):
    lists.append(eval(input("please input a number: ")))
print(lists)
"""
"""
keep_going = True

items = []
while keep_going:
    lists.append(eval(input("please input a number: ")))
    keep_going = eval(input("Do you want to continue True/False: "))

print(lists)
"""
# Entering the values of a list in one go: Building a list from user without a loop
data = eval(input("Enter your values"))

print(data)

data.insert(3, 1000)  # insert at index 3

print(data.index(1000))

data.sort()

print(data)

data.reverse

print(data)

del data[3]

print(data)
