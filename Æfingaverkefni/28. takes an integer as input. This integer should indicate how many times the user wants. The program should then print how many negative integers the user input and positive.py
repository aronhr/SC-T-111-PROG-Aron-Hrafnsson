turns = int(input("how many times: "))
negative = []
positive = []

for x in range(1, turns + 1):
    i = int(input("Enter a number: "))
    if i < 0:
        negative.append(i)
    elif i > 0:
        positive.append(i)

print("Negative " + str(len(negative)))
print("Positive " + str(len(positive)))
