input("How many numbers will you enter?")


def check(arr):
    return 20 > len(arr) > 2


def main():
    numbers = [int(ss) for ss in input().split()]

    if check(numbers):
        print("The smallest number is", min(numbers))
    else:
        print("Wrong len of numbers")


main()
