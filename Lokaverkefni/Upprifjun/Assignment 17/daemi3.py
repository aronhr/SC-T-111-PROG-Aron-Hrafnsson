"""
Design a class called Sentence that has a constructor that takes a string
representing the sentence as input.  The class should have the following methods:

get_first_word(): returns the first word as a string
get_all_words(): returns all words in a list.
replace(index, new_word): Changes a word at a particular index to "new_word".
For example, if sentences is "I'm going back", then replace(2, "home") results in
"I'm going home".  If the index is not valid, the method does not do anything.
"""


class Sentence(object):
    def __init__(self, sentence=""):
        self.__sentence = sentence

    def get_first_word(self):
        a = self.__sentence.split()
        return a[0]

    def get_all_words(self):
        return self.__sentence.split()

    def replace(self, index, new_word):
        word = self.__sentence.split()
        word[index] = new_word
        self.__sentence = " ".join(word)
        return self.__sentence

sent = Sentence('This is a test')
print(sent.get_first_word())
assert str(sent.get_first_word()) == "This"

print(sent.get_all_words())
assert sent.get_all_words() == 'This is a test'.split()

sent.replace(3, "must")
print(sent.get_all_words())
assert sent.get_all_words() == 'This is a must'.split()