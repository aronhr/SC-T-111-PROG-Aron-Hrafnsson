"""
Write a program that keeps asking the user for new values to be added to a list until the user
enters 'exit' ('exit' should NOT be added to the list). After that, the program creates a new
list with 3 copies of every value in the initial list.  Finally, the program prints out all
of the values in the new list.

Your program needs to be able to handle any variation of 'exit' such as 'Exit', 'EXIT' etc.
and treat them all as 'exit'.

The main program is given - DO NOT change it.

Example input/output:

Enter value to be added to list: a

Enter value to be added to list: b

Enter value to be added to list: c

Enter value to be added to list: exit

a
b
c
a
b
c
a
b
c

"""
arr = []
i = input("Enter value to be added to list: ")

while i != "exit":
    arr.append(i)
    i = input("Enter value to be added to list: ")

print(arr)
