# Constants to be used in the implementation
DIM = 5
POSITION = 'o'
EMPTY = 'x'
LEFT = 'l'
RIGHT = 'r'
UP = 'u'
DOWN = 'd'
QUIT = 'q'


def get_move():
    ''' Returns a move corresponding to the user input direction '''
    move = input('Move: ')

    if move not in [LEFT, RIGHT, UP, DOWN]:
        return QUIT
    else:
        return move


def initialize_grid(x, y):
    ''' Returns an initialized grid for the given dimension '''
    grid = []

    for i in range(DIM):
        sublist = []
        for j in range(DIM):
            sublist.append(EMPTY)
        grid.append(sublist)

    grid[x][y] = POSITION  # Current position
    return grid

# Main program starts here
# In your implementation, you have to use the functions and the constants given above


def move(m, x, y):
    if m == LEFT:
        x += 0
        y += -1
    elif m == RIGHT:
        x += 0
        y += 1
    elif m == UP:
        x += -1
        y += 0
    elif m == DOWN:
        x += 1
        y += 0
    return x, y


def main():
    x = 0
    y = 0
    grid = initialize_grid(x, y)
    while True:
        for line in grid:
            print(*line)

        request = get_move()

        if request == QUIT:
            exit(0)
        else:
            try:
                x, y = move(request, x, y)
                grid = initialize_grid(x, y)
            except IndexError:
                pass


main()
