value = int(input("Initial value: "))
step = int(input("Step: "))
samtals = value
summa = 0
steps = step
print(samtals, end=" ")

while samtals <= 100:
        summa = value + steps
        print(summa, end=" ")
        steps += step
        samtals = samtals + summa

print("\nSum of series: " + str(samtals))
