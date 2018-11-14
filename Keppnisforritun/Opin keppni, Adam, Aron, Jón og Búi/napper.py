i = int(input())

for x in range(1, i+1):
    z = input().split()
    if int(z[1]) % 2 == 0:
        print("Case #" + str(x) + ": OFF")
    else:
        print("Case #" + str(x) + ": ON")
