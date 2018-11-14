def main():
    e = input("Enter an character: ")
    if e.islower():
        print(e.upper())
    elif e.isupper():
        print(e.lower())


def string_remake():
    e = input("Enter an word: ")
    b = []
    for x in e:
        if x.isupper():
            b.append(x.lower())
        elif x.islower():
            b.append(x.upper())
    return ''.join(b)


main()
print(string_remake())
