def lowest_value(nums):
    return min(nums)


def check(length, l):
    return len(length) == l


def main():
    for x in range(2, 5):
        i = [int(ss) for ss in input("Enter " + str(x) + " numbers: ").split(',')]
        if x == 4:
            print(lowest_value(i))
        else:
            if check(i, x):
                print(lowest_value(i))
            else:
                print("What the fuck?!?!?")


main()
