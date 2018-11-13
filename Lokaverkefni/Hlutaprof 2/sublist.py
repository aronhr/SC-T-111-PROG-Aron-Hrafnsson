def make_sublists(listi):
    subs = [[]]
    for i in range(len(listi)):
        n = i + 1
        while n <= len(listi):
            sub = listi[i:n]
            subs.append(sub)
            n += 1
    return subs


# Main program starts here
def main():
    listi = input("Enter a list separated with commas: ").split(',')
    sub_lists = make_sublists(listi)

    print(sorted(sub_lists))


# This should be the last statement in your main program/function
main()
