size = int(input("Input size: "))

arr = []
for i in range(size):
    arr.append(int(input("Enter value {}:".format(i + 1))))

target = int(input("Input target"))
# Demo 1
if target in arr:
    print("{} is in the list.".format(target))
else:
    print("{} is not in the list.".format(target))

# Demo 2
found = 0
for a in arr:
    if target == a:
        found += 1

if found:
    print("{} is {} in the list.".format(target, found))
else:
    print("{} is {} in the list.".format(target, found))
