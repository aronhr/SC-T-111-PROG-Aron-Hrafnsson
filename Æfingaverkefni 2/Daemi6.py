def size(i: int):
    value = []
    for x in range(i):
        value.append(int(input("Enter some value: ")))
    return sum(value)


s = size(int(input("Enter size of list: ")))
print(s)
