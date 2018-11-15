import string
"""
Write a program that makes a list of the unique letters in an input sentence.
That is, if the letter "x" is used twice in a sentence, it shouild only appear once in your list.
Neither punctuation nor white space should appear in your list.
"""

sentence = input("Enter sentence: ").strip().replace(" ", "")

arr = []
for x in sentence:
    if x not in arr:
        if x in string.punctuation:
            continue
        arr.append(x)

print(arr)
