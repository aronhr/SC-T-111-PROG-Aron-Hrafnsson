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
found = False
for a in arr:
    if target == a:
        found = True

if found:
    print("{} is in the list.".format(target))
else:
    print("{} is not in the list.".format(target))
