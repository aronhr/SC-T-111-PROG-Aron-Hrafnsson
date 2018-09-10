low = int(input("Enter lower number: "))
high = int(input("Enter higher number: "))
sums = 0

for x in range(low, high + 1):
    sums = sums + x

print(sums)
