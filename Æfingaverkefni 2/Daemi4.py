def size(i: int):
    value = []
    for x in range(i):
        value.append(input("Enter some value: "))
    return max(value)


print(size(int(input("Enter size of list: "))))