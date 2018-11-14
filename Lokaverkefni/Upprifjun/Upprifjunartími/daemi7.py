size = int(input("Input size: "))

arr = []
for i in range(size):
    arr.append(int(input("Enter value {}:".format(i + 1))))

summs = 0

for x in range(1, len(arr)):
    summs += arr[x]

print("{:.2f} is the average".format(summs/len(arr)))
