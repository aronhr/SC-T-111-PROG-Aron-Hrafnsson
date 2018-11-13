x = int(input("Initial value: "))
y = int(input("Step: "))
sum = 0

while sum <= 100:
    sum += x
    print(x, end=" ")
    x += y

print("\nSum of series: " + str(sum))
