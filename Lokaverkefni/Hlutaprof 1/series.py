value = int(input("Initial value: "))
step = int(input("Step: "))
summa = 0

while summa <= 100:
    summa += value
    print(value, end=" ")
    value += step

print("\nSum of series: " + str(summa))
