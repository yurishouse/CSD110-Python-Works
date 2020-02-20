
#  List comprehension

# Old style: build a list of 10 squares of even numbers
values = []

for i in range(1, 11):
    if i % 2 == 0:
        values.append(i**2)

print(values)

# New Style using  List comprehension

numbers = [x**2 for x in range(1, 11) if x % 2 == 0]

print(numbers)

list2 = [x for x in range(11)]

print(list2)
