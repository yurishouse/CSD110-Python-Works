# Made by Shiina Yuri

# The first Line (4  5  6  7  8  9  10)

for i in range(4, 11, 1):
    print(i, end=' ')

print()  # empty line

# The second line (6  5  4  3  2  1)

for i in range(6, 0, -1):
    print(i, end=' ')

print()  # empty line

# The third line (2  4  6  8  10  12  14  16)

for i in range(2, 17, 2):
    print(i, end=' ')

print()  # empty line

# The forth line (19  17  15  13  11  9  7  5)

for i in range(19, 4, -2):
    print(i, end=' ')

print()  # empty line

# The fifth line (7  15  23  31  39)

for i in range(7, 40, 8):
    print(i, end=' ')

print()  # empty line

# The Sixth line (2  4  8  16  32  64)

for i in range(1, 7):
    i = 2 ** i
    print(i, end=' ')
