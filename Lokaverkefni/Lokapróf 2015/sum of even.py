def read_numbers():
    return [int(ss) for ss in input().split()]


def sum_of_even(tolur):
    t = []
    for x in tolur:
        if x % 2 == 0:
            t.append(x)
    return sum(t)


def main():
    print("Sum of even numbers:", sum_of_even(read_numbers()))


main()
