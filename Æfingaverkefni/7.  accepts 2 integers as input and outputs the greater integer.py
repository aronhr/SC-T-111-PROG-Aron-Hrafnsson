a = int(input("Enter integer: "))
b = int(input("Enter another integer:"))
a = str(a)
b = str(b)
if a > b:
    print(a + " is grater then " + b)
elif b > a:
    print(b + " is grater then " + a)
elif a == b:
    print(a + " is equal to " + b)
else:
    print("What the fuck?")
