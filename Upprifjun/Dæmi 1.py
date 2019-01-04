import random

TEAM_SIZE = 11
GAME_LENGTH = 90


class Team:
    def __init__(self, name):
        self.__name = name
        self.__team = []
        self.__points = 0
        for i in range(TEAM_SIZE):
            player = FootballPlayer(i + 1)  # i+1 is the number for the player
            self.__team.append(player)

    def play_offence(self):
        random_index = random.randint(0, TEAM_SIZE - 1)
        self.__points += self.__team[random_index].shoot_ball()

    def get_player_with_highest_score(self):
        highest_player = self.__team[0]
        for player in self.__team:
            if player > highest_player:
                highest_player = player
        return highest_player

    def get_name(self):
        return self.__name

    def get_points(self):
        return self.__points

    def __str__(self):
        the_str = ''
        for player in self.__team:
            the_str += str(player)
        return the_str


class FootballPlayer:
# You need to implment this class


def print_winner(team_a, team_b):
    ''' You need to implement this function. Print out:
        which team won (if tie, print "Tie!")
    '''



def print_scores(team_a, team_b):
    ''' You need to implent this function.  Print out:
        how many points each team scored
        the scoring of each player in each team
        the highest scoring player in each team
    '''



def play(team_a, team_b):
    for _ in range(GAME_LENGTH):
        team_a.play_offence()
        team_b.play_offence()


def random_seed():
    random.seed(30)


def main():
    # You are not allowed to change this main function
    random_seed()
    team1 = Team("Fjölnir")
    team2 = Team("KR")

    play(team1, team2)
    print_winner(team1, team2)
    print_scores(team1, team2)


main()
