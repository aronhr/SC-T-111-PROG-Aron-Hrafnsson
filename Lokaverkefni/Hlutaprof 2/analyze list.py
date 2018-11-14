def is_prime(n):
    '''Returns True if the given positive number is prime and False otherwise'''
    if n == 1:
        return False
    if n == 2:
        return True
    for i in range(2, n):
        if n % i == 0:
            return False
    else:
        return True


def print_list(listi):
    return [int(ss) for ss in listi]


def prime(listi):
    prime_list = []
    for x in listi:
        if is_prime(x) and x not in prime_list:
            prime_list.append(x)
    return prime_list


# The main program starts here
def main():
    try:
        l = input("Enter integers separated with commas: ").split(',')
        print("Input list:", print_list(l))
        print("Sorted list:", sorted(print_list(l)))
        print("Prime list:", sorted(prime(print_list(l))))
        print("Min: {}, Max: {}, Average: {:.2f}".format(min(print_list(l)), max(print_list(l)), (sum(print_list(l))/len(l))))
    except ValueError:
        print("Incorrect input!")


main()
