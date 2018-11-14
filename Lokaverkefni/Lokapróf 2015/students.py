class Players(object):
    def __init__(self, name, year):
        self.name = name
        self.year = year

    def __str__(self):
        return "Name: {} \nYear: {} \n".format(self.name, self.year)


def get_highest_rated_player(players):
    highest = 0
    for x in players:
        if float(x[1]) > highest:
            highest = float(x[1])
            h = Players(x[0], x[1])
    return h


def get_average_rating(players):
    rating = 0
    for x in players:
        rating += float(x[1])
    return "{:.3f}".format(rating / len(players))


def main():
    number_of_players = int(input("Number of Students: "))
    players = []

    print("--- Reading Students ---")
    for x in range(number_of_players):
        name = input("Name: ")
        year = float(input("Grade: "))
        print('')
        players.append([name, year])

    print("--- Displaying Students --- ")
    for x in players:
        print(Players(x[0], x[1]))

    highest_rated_player = get_highest_rated_player(players)
    print("Highest Student: ")
    print(highest_rated_player)

    average_rating = get_average_rating(players)
    print("Average grade:", average_rating)


main()
