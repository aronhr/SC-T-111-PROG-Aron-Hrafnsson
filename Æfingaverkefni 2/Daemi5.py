def size(i: int):
    value = []
    for x in range(i):
        value.append(input("Enter some value: "))
    return min(value)


print(size(int(input("Enter size of list: "))))