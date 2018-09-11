u = ""
arr = []

while u != "n":
    number = float(input("Please enter a real number: "))
    arr.append(number)
    u = input("Do you wish to enter another number (y=yes): ")

m = sum(arr) / len(arr)

print("Average of all numbers: " + str(m))
