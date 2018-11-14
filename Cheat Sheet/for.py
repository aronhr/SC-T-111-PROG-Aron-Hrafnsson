"""
Print each fruit in a fruit list:

apple
banana
cherry
"""
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)


"""
Loop through the letters in the word "banana":

b
a
n
a
n
a
"""
for x in "banana":
    print(x)

"""
Exit the loop when x is "banana":

apple
banana
"""
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
    if x == "banana":
        break

"""
Exit the loop when x is "banana", but this time the break comes before the print:
apple
"""
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        break
    print(x)

"""
Do not print banana:

apple
cherry
"""
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        continue
    print(x)


"""
Using the range() function:

0
1
2
3
4
5
"""
for x in range(6):
    print(x)

"""
Using the start parameter:

2
3
4
5
"""
for x in range(2, 6):
    print(x)

"""
Increment the sequence with 3 (default is 1):

2
5
8
11
14
17
20
23
26
29
"""
for x in range(2, 30, 3):
    print(x)

"""
Print all numbers from 0 to 5, and print a message when the loop has ended:

0
1
2
3
4
5
Finally finished!
"""
for x in range(6):
    print(x)
else:
    print("Finally finished!")

"""
Print each adjective for every fruit:

red apple
red banana
red cherry
big apple
big banana
big cherry
tasty apple
tasty banana
tasty cherry
"""
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
    for y in fruits:
        print(x, y)


"""
Recursion Example



Recursion Example Results
1
3
6
10
15
21
"""


def tri_recursion(k):
    if k > 0:
        result = k+tri_recursion(k-1)
        print(result)
    else:
        result = 0
    return result


print("\n\nRecursion Example Results")
tri_recursion(6)

