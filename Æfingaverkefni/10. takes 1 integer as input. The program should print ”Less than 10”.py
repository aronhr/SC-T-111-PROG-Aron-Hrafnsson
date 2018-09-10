i = int(input("Enter integer: "))

if i < 10 and i > 0:
    print("Less than 10")
elif i >= 10 and i < 20:
    print("between 10 and 20")
elif i >= 20:
    print("the value is too high!")
else:
    print("too low")
