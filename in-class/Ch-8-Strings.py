

message = 'This is a string'

print(message)

bigString = """
233
66
999
114514
"""

print(bigString)

for char in message:
    print(char, end=' ')

print()

print('character index 11', message[11])


days = ['Mon', 'Tue']

x = input('Temp for ' + days[0])

y = x + message

print(x, ' ', y)

# slicing
# string[start: end: step]

aStr = message[8: 16]

print(aStr)

