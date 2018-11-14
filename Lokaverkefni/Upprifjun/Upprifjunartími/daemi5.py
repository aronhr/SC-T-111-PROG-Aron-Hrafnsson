size = int(input("Input size: "))

arr = []
for i in range(size):
    arr.append(int(input("Enter value {}:".format(i + 1))))

lowest = float("inf")

for x in range(1, len(arr)):
    if arr[x] < lowest:
        highest = arr[x]

print("{} is the lowest".format(lowest))
