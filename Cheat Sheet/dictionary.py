"""
Create and print a dictionary:

{'brand': 'Ford', 'model': 'Mustang', 'year': 1964}
"""
thisdict={
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)

"""
Get the value of the "model" key:

Mustang
"""
x = thisdict["model"]

"""
Change the "year" to 2018:

"""
thisdict["year"] = 2018

"""
Print all key names in the dictionary, one by one:

brand
model
year
"""
for x in thisdict:
    print(x)

"""
Print all values in the dictionary, one by one:

Ford
Mustang
2018
"""
for x in thisdict:
    print(thisdict[x])

"""
You can also use the values() function to return values of a dictionary:

Ford
Mustang
2018
"""
for x in thisdict.values():
    print(x)

"""
Loop through both keys and values, by using the items() function:

brand Ford
model Mustang
year 2018
"""
for x, y in thisdict.items():
    print(x, y)


"""
Check if "model" is present in the dictionary:

Yes, 'model' is one of the keys in the thisdict dictionary
"""

if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")

"""
Print the number of items in the dictionary:

3
"""
print(len(thisdict))


"""
Adding an item to the dictionary is done by using a new index key and assigning a value to it:

{'brand': 'Ford', 'model': 'Mustang', 'year': 2018, 'color': 'red'}
"""
thisdict["color"] = "red"
print(thisdict)

"""
The pop() method removes the item with the specified key name:

{'brand': 'Ford', 'year': 2018, 'color': 'red'}
"""
thisdict.pop("model")
print(thisdict)

"""
The popitem() method removes the last inserted item (in versions before 3.7, a random item is removed instead):

{'brand': 'Ford', 'year': 2018}
"""
thisdict.popitem()
print(thisdict)


"""
The del keyword removes the item with the specified key name:

{'year': 2018}
"""
del thisdict["brand"]
print(thisdict)




