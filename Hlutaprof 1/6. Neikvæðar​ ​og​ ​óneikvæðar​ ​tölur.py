howmany = int(input("How many number")) #hversu margar töluv eigar vera i boði
negative = []
positive = []
for i in range(1, howmany + 1): # tölur frá 1 til hversu margar voru skrifaðar
    x = float(input("Enter a number: "))
    if x < 0:
        negative.append(x)
    else:
        positive.append(x)

print("Negative numbers:" + str(len(negative)))
print("Non-negative numbers: " + str(len(positive)))
print("Sum of non-negative numbers: " + str(sum(positive)))