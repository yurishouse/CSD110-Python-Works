# Create an empty set

set1 = set()

print(set1)

set2 = set("Python")

print(set2)

name = "SEaTtle"

nameSet = set(name)

print(nameSet)

list1 = [12, 14, 16, 18, 2, 0, 22, 2, 4, 26, 2, 8, 30]
print(list1)
list1Set = set(list1)
print(list1Set)
list1 = list(list1Set)
print(list1, "After")

total = 0
for item in list1Set:
    total += item
print("total value in the list set=", total)

setA = set("abcdefgh")

item = 'a'

if item in setA:
    print("Found")
else:
    print("Not Found")

item2 = 'z'

if item2 not in setA:
    print("z is not in set A")


setA.add('z')

print(setA)


numbers = set()
keep = True

while keep:
    numbers.add(eval(input('Enter a number to the set: ')))
    keep = eval(input("continue? True/False"))
print(numbers)
