k = int(input())
for z in range(k):
    i = [int(ss) for ss in input().split()]
    arr = []
    for x in range(i[0]):
        arr.append(list(input()))

    print("Test", z+1)
    arr.reverse()
    for y in arr:
        print(''.join(y[::-1]))
