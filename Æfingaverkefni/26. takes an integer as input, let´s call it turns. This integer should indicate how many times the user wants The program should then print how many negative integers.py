turns = int(input("how many times: "))
arr = []

for x in range(1, turns + 1):
    i = int(input("Enter a number: "))
    if i < 0:
        arr.append(i)
print(len(arr))

