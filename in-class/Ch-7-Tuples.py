import math

# Create a tuple
list1 = [0, 44, 35]

rec = tuple(list1)  # Convert a list to a tuple

list2 = list(rec)  # convert a tuple to a list

print(rec)
print(list2)

# Try to Update a value in the tuple
# rec[0] = 77 (Does not work)


for item in rec:
    print(item)

x, y, z = 12, 44, 65

d1, d2, d3 = rec

print(d1, d2, d3)

# create a record

familyRec = ("Yuri", "425-961-8844", "Address", "114514")

name, phone, address, sid = familyRec

print(name, sid, address, phone)


def circle_measure(radius):
    area = math.pi * radius ** 2
    perimeter = 2 * math.pi * radius
    return area, perimeter


# collecting the two returned values in a tuple

cirMes = circle_measure(30)

area1, perimeter1 = circle_measure(20)

print(cirMes)
print(area1, perimeter1)

# given a list: [34, 56, 78]
# 2 ways of assign the variable

data = [34, 56, 78]
a, b, c = data

# 1st way : indexing
a1 = data[0]
b1 = data[1]
c1 = data[2]

# 2nd way : using tuple
tup = tuple(data)
x1, y1, z1 = tup

# One shot
f, g, h = data
