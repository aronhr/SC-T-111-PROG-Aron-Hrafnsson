i = int(input())
for x in range(i):
    arr = []
    s = int(input())
    for y in range(s):
        k = input()
        if k not in arr:
            arr.append(k)

    print(len(arr))
