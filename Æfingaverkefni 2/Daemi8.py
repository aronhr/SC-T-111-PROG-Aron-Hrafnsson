def size(i: int):
    value = []
    for x in range(i):
        value.append(input("Enter some value: "))
    return value


def check_target(value):
    v = []
    for z in value:
        if z not in v:
            v.append(z)
    return v


s = size(int(input("Enter size of list: ")))
print(check_target(s))
