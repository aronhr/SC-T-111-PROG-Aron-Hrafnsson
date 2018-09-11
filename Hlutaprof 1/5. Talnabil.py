lower = int(input("lower: "))
higer = int(input("higher: "))
between = 0

while True:
 between = int(input("enter number between " + str(lower) + " and " + str(higer) + ":"))

 if(lower <= between <= higer):
        print("Gotham city is safe … for now")
        break
