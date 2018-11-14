size = int(input("Input size: "))

arr = []
for i in range(size):
    arr.append(int(input("Enter value {}:".format(i + 1))))

summs = 0

for x in range(1, len(arr)):
    summs += arr[x]

print("{} is the sum".format(summs))
