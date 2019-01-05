"""
Þú átt að útfæra clasann DiceThrower í honum á að vera
Constructor sem skilgreinir hversu marga tenginga notandinn hefur, breytu sem kallar í Dice classan
throw fall sem kastar öllum teningunum í lista
rethow fall kastar völdum tenginum aftur

Einnig áttu að búa til 2 föll
Main_menu sem býr prentar út upphafið á leiknum og tekur inn input frá notenda hvað hann vill gera
Print_sheet sem prentar út stigatöflu notenda

Dæmi:

1: New game
2: Quit

Enter your choice(1/2)please: 1
[4, 5, 4, 2, 2]
Do you want to Rethrow? (Y/N): y
Enter the dices you want to rethrow (0 - 4) space between please: 1
[4, 3, 4, 2, 2]
Do you want to Rethrow? (Y/N): y
Enter the dices you want to rethrow (0 - 4) space between please: 1
[4, 1, 4, 2, 2]

0: Small Row 0
1: Big Row 0
2: Full House 0
3: Chance 0
4: Yatzy 0
Enter your choice(0 - 4)please: 4

0: Small Row 0
1: Big Row 0
2: Full House 0
3: Chance 0
4: Yatzy 13
[1, 4, 3, 5, 5]
Do you want to Rethrow? (Y/N): y
Enter the dices you want to rethrow (0 - 4) space between please: 0 1 2
[5, 1, 3, 5, 5]
Do you want to Rethrow? (Y/N): y
Enter the dices you want to rethrow (0 - 4) space between please: 0 1
[6, 3, 3, 5, 5]

0: Small Row 0
1: Big Row 0
2: Full House 0
3: Chance 0
4: Yatzy 13
Enter your choice(0 - 4)please: 0

0: Small Row 22
1: Big Row 0
2: Full House 0
3: Chance 0
4: Yatzy 13
[1, 4, 4, 5, 6]
Do you want to Rethrow? (Y/N): n

0: Small Row 22
1: Big Row 0
2: Full House 0
3: Chance 0
4: Yatzy 13
Enter your choice(0 - 4)please: 2

0: Small Row 22
1: Big Row 0
2: Full House 20
3: Chance 0
4: Yatzy 13
[2, 3, 3, 4, 6]
Do you want to Rethrow? (Y/N): n

0: Small Row 22
1: Big Row 0
2: Full House 20
3: Chance 0
4: Yatzy 13
Enter your choice(0 - 4)please: 2

0: Small Row 22
1: Big Row 0
2: Full House 18
3: Chance 0
4: Yatzy 13
[4, 1, 2, 3, 4]
Do you want to Rethrow? (Y/N): n

0: Small Row 22
1: Big Row 0
2: Full House 18
3: Chance 0
4: Yatzy 13
Enter your choice(0 - 4)please: 2

0: Small Row 22
1: Big Row 0
2: Full House 14
3: Chance 0
4: Yatzy 13
Final Score 49
1: New game
2: Quit

Enter your choice(1/2)please: 2

Process finished with exit code 0

"""


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

    user_input = input('Enter your choice(1/2)please: ')

    if user_input == "1":
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

        print(user_dice)

        while rethrowing_allowed:
            rethrow = input('Do you want to Rethrow? (Y/N): ').upper()
            if rethrow == 'Y':
                s = input("Enter the dices you want to rethrow (0 - 4) space between please: ")
                dice = s.split()
                rethrow_dice = [eval(x) for x in dice]

                user_dice = dice_thrower.rethrow(rethrow_dice)
                number_of_throws += 1

                print(user_dice)
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


def main():
    # Do not change this code
    dt = DiceThrower()
    sheet = [0, 0, 0, 0, 0]
    game_is_on = main_menu()

    while game_is_on:
        for i in range(0, 5):
            dice = dice_menu(dt)
            sheet_menu(dice, sheet)

        print('Final Score', sum(sheet))
        game_is_on = main_menu()


main()
