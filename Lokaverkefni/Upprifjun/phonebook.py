"""
VIRKAR ÁN CLASS
"""

class Contact(object):
    def __init__(self, name, phone, address):
        self.__name = name
        self.__phone = phone
        self.__address = address

    def set_name(self, other):
        self.__name = other

    def set_phone(self, other):
        self.__phone = other

    def set_address(self, other):
        self.__address = other

    def get_name(self):
        return self.__name

    def get_phone(self):
        return self.__phone

    def get_address(self):
        return self.__address

    def __str__(self):
        return "Name: {} Phone number: {} Address: {}".format(self.get_name(), self.get_phone(), self.get_address())


def add_contact(contacts):
    cname = input("Enter name: ")
    cnumber = input("Enter number: ")
    caddress = input("Enter address: ")
    contacts[cname] = [cnumber, caddress]
    return contacts


def edit_contact(contacts):
    i = input("Name to locate: ")
    if i in contacts.keys():
        print(*contacts[i])
        cnumber = input("Enter number: ")
        caddress = input("Enter address: ")
        contacts[i] = [cnumber, caddress]
    else:
        print("Contact does not exist!")


def remove_contact(contacts):
    i = input("Name to locate: ")
    if i in contacts.keys():
        print(*contacts[i])
        contacts.pop(i)
        print("Contact removed!")
    else:
        print("Contact does not exist!")


def main():
    contacts = {}
    while True:
        print("1. Add Contact")
        print("2. Edit Contact")
        print("3. Remove Contact")
        print("4. Print Phonebook")
        print("5. Exit")

        val = input()

        if val == "1":
            contacts = add_contact(contacts)
        elif val == "2":
            edit_contact(contacts)
        elif val == "3":
            remove_contact(contacts)
        elif val == "4":
            print(contacts)
        elif val == "5":
            exit(0)


main()
