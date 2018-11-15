def is_prime(n):
    if n == 1:
        return False
    i = 2
    while i*i <= n:
        if n % i == 0:
            return False
        i += 1
    return True


def main():
    n = int(input())
    for x in range(1, n):
        for y in range(1, n):
            for z in range(1, n):
                if (x + y + z) == n:
                    print("{} {} {}".format(x, y, z))
                    exit(0)
    else:
        print("Neibb")


main()
