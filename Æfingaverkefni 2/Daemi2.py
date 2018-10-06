def size(i: int):
    value = []
    for x in range(i):
        value.append(input("Enter some value: "))
    return value


def check_target(x, value):
    if x in value:
        v = x + " is in the list"
    else:
        v = x + " is not in the list"
    return v


s = size(int(input("Enter size of list: ")))
print(check_target(input("Search for target: "), s))
