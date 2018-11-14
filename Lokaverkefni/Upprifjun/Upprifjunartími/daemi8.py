size = int(input("Input size: "))

arr = []
for i in range(size):
    arr.append(int(input("Enter value {}:".format(i + 1))))
new_list = []

for x in range(1, len(arr)):
    if x not in new_list:
        new_list.append(x)

print("The list: {}".format(arr))
print("The list with no duplicates: {}".format(new_list))
