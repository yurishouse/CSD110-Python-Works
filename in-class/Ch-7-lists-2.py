numbers = [7, 5, 3, 4, 77, 44, 55, 64, 74]

print(numbers[:])  # everything

print(numbers[::2])  # every other element

print(numbers[1:5])  # a slice 1-4

sub_numbers = numbers[2:7]  # Create a sublist 2-6

print(sub_numbers)

# the "in" operaator
# we use it in a loop to go over all elements
# we also use in if statement to check if the itemlist
# contains an item / element

item = 11

# check if item is in the numbers list

if item in numbers:
    print("Yahoo!")
else:
    print("Kahoot!")

