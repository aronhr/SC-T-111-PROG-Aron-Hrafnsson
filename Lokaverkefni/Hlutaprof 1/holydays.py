manudur = input("Mánuður: ")
dagur = input("Dagur: ")

summa_daga = manudur.capitalize() + " " + dagur

if summa_daga == "January 1":
    print("New year's day")
elif summa_daga == "June 17":
    print("National holiday")
elif summa_daga == "December 25":
    print("Christmas day")
else:
    print("Not a holiday")
