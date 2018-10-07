def size(i: int):
    value = []
    for x in range(i):
        value.append(input("Enter some value: "))
    return value


def check_target(value):
    x = input("Search for target: ")
    v = []
    for z in range(len(value) - 1):
        if x in value:
            v.append(x)
    return len(v)


s = size(int(input("Enter size of list: ")))
print(check_target(s))
