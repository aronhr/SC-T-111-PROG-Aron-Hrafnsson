a = int(input("Enter number one: "))
b = int(input("Enter number two: "))
c = int(input("Enter command (1: add a and b, 2:  subtract b from a, 3: multiply a and b)"))

if c == 1:
    print(a + b)
elif c == 2:
    print(b - a)
elif c == 3:
    print(a * b)
else:
    print("invalid input.")
