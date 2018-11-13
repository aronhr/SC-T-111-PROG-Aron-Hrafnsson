# Function definitions start here
def open_file(file_name):
    try:
        with open(file_name, "r") as text_file:
            word_string = ""
            for line in text_file:
                word_string += line
            return word_string.split()
    except FileNotFoundError:
        return None


def get_longest_word(file):
    longest = ""
    for x in file:
        if len(x) > len(longest):
            longest = x

    return longest


# The main program starts here
filename = input("Enter name of file: ")
file_stream = open_file(filename)
if file_stream:
    longest_word = get_longest_word(file_stream)
    print("Longest word is '{:s}' of length {:d}".format(longest_word, len(longest_word)))
else:
    print('File', filename, 'not found!')
