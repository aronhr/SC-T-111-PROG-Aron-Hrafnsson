def get_file(file_name):
    try:
        with open(file_name, "r", encoding="utf-8") as data_file:
            data_list = []  # start with an empty list
            for line_str in data_file:
                data_list.append(line_str.strip().split())
            return sorted(data_list)
    except FileNotFoundError:
        print("Cannot find file", file_name)


def list_to_dic(a_dict):
    dic = {}
    for x in a_dict:
        if x[0] not in dic.keys():
            dic[x[0]] = x[1]
        else:
            dic[x[0]] += " " + x[1]
    return dic


def print_people(a_dict):
    john = -1
    mary = -1
    phil = -1
    for x in a_dict.keys():
        print(x + ": ")

        countries = a_dict[x].split()
        arr = []
        count = []
        for y in countries:
            if y not in arr:
                arr.append(y)
                print("\t", y)
            count.append(y)
        if x == "John":
            john += len(count)
        elif x == "Mary":
            mary += len(count)
        elif x == "Phil":
            phil += len(count)

    if john >= mary > phil:
        print("John has been to {} countries".format(john))
    elif mary > john > phil:
        print("Mary has been to {} countries".format(mary))
    elif phil > john > mary:
        print("Phil has been to {} countries".format(phil))



file_name = "flights.txt"
file = get_file(file_name)
dic = list_to_dic(file)
print_people(dic)
