low = int(input("Enter lower number: "))
high = int(input("Enter higher number: "))
sums = 0

for x in range(low, high + 1):
    if x % 3 == 0 or x % 5 == 0:
        sums = sums + x

print(sums)
