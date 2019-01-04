import random


class Dice:
    def __init__(self):
        self.number = 0

    def throw(self):
        self.number = random.randint(1, 6)
        return self.number


class DiceThrower:
    def __init__(self, how_many=5):
        self.number_of_dice = how_many
        self.dice = Dice()
        self.dice_list = [-1 for i in range(self.number_of_dice)]

    def throw(self):
        for x in range(0, self.number_of_dice):
            self.dice_list[x] = self.dice.throw()
        return self.dice_list

    def rethrow(self, rethrow_list=[]):
        if 0 < len(rethrow_list) <= self.number_of_dice:
            if min(rethrow_list) >= 0 and max(rethrow_list) <= self.number_of_dice - 1:
                for item in rethrow_list:
                    self.dice_list[item] = self.dice.throw()
            return self.dice_list
        else:
            return self.throw()


def main_menu():
    print('1: New game')
    print('2: Quit')
    print()

    user_input = int(input('Enter your choice(1/2)please: '))

    if user_input == 1:
        return True
    else:
        return False


def dice_menu(dice_thrower):
    still_throwing = True
    number_of_throws = 0

    while still_throwing:
        user_dice = dice_thrower.throw()
        number_of_throws += 1
        rethrowing_allowed = True

        print()
        print(user_dice)
        print()

        while rethrowing_allowed:
            rethrow = input('Do you want to Rethrow? Y/N: ')
            if rethrow == 'Y':
                s = input("Enter the dices you want to rethrow(0 - 4) space between please: ")
                dice = s.split()
                rethrow_dice = [eval(x) for x in dice]

                user_dice = dice_thrower.rethrow(rethrow_dice)
                number_of_throws += 1

                print()
                print(user_dice)
                print()
            else:
                rethrowing_allowed = False

            if number_of_throws == 3:
                rethrowing_allowed = False

        still_throwing = False

    return user_dice


def sheet_menu(dice, yatzy_sheet):
    print_sheet(yatzy_sheet)
    user_input = int(input('Enter your choice(0 - 4)please: '))
    yatzy_sheet[user_input] = sum(dice)
    print_sheet(yatzy_sheet)


def print_sheet(yatzy_sheet):
    print()
    print('0: Small Row', yatzy_sheet[0])
    print('1: Big Row', yatzy_sheet[1])
    print('2: Full House', yatzy_sheet[2])
    print('3: Chance', yatzy_sheet[3])
    print('4: Yatzy', yatzy_sheet[4])
    print()


dt = DiceThrower()
sheet = [0, 0, 0, 0, 0]
game_is_on = main_menu()

while game_is_on:
    for i in range(0, 5):
        dice = dice_menu(dt)
        sheet_menu(dice, sheet)

    print('Final Score', sum(sheet))
    game_is_on = main_menu()

print('The End!')
