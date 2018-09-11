month = input("Month: ")
day = int(input("Day: "))

manudur = month[0].upper() + month[1:] + " " + str(day)

if manudur == "January 1":
    print("New year's day")
elif manudur == "June 17":
    print("National holiday")
elif manudur == "December 25":
    print("Christmas day")
else:
    print("Not a holiday")
