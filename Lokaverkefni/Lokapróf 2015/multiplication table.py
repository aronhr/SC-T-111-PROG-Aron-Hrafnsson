def get_value():
    val = int(input("Input table size: "))
    if 0 < val > 8:
        print("Invalid size!")
        exit(0)
    return val


def main(val):
    for x in range(1, val + 1):
        print("{}|".format(x), end="")
        for y in range(1, val + 1):
            print("{}".format("\t" + str((x*y))), end="")
        print("")


def header(val):
    for x in range(1, val + 1):
        print("{}".format("\t" + str(x)), end="")
    print("")
    print("\t" + ("-" * (4*val)))


value = get_value()
header(value)
main(value)
