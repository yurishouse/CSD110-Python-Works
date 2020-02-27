A = set("abcd")
B = set('cdfg')
print("A =", A, "B =", B)

# Union operation

union = A | B
print("A union B =", union)

# Intersection op

inter = A & B
print("A Intersect B=", inter)

# Difference op

diff1 = A - B

print("A - B =", diff1)

diff2 = B - A

print("B - A =", diff2)

# Symmetrical difference

sydiff = A ^ B

print("A ^ B=", sydiff)

# Check if A is a subset of B

if A <= B:
    print("A is a subset of B")
else:
    print("A is not a subset of B")
