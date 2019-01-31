import random
import os 

CELLS = [
    (0,0),(1,0),(2,0),(3,0),(4,0),
    (0,1),(1,1),(2,1),(3,1),(4,1),
    (0,2),(1,2),(2,2),(3,2),(4,2),
    (0,3),(1,3),(2,3),(3,3),(4,3),
    (0,4),(1,4),(2,4),(3,4),(4,4)
]

def clearScreen():
    os.system('cls' if os.name == 'nt' else 'clear')


def locations():
    return random.sample(CELLS, 3)

def movePlayer(player, move):
    x, y = player
    if move == "LEFT":
        x -= 1
    if move == "RIGHT":
        x += 1
    if move == 'UP':
        y -= 1
    if move == 'DOWN':
        y += 1
    else:
        print('Please choose a valid option from the moves')
    return x, y


def getMoves(player):
    moves = ['LEFT', 'RIGHT', 'UP', 'DOWN']
    x, y = player
    if x == 0: 
        moves.remove('LEFT')
    if x == 4:
        moves.remove('RIGHT')
    if y == 0: 
        moves.remove('UP')
    if y == 4: 
        moves.remove('DOWN')
    return moves


def drawMap(player):
    print(' _' * 5)
    tile = '|{}'
    for cell in CELLS:
        x, y = cell
        if x < 4:
            lineEnd = ''
            if cell == player:
                output = tile.format('X')
            else:
                output = tile.format('_')
        else:
            lineEnd = '\n'
            if cell == player:
                output = tile.format('X|')
            else:
                output = tile.format('_|')
        print(output, end=lineEnd)

def gameLoop():
    monster, door , player = locations()
    playing = True

    while playing:
        clearScreen()
        validMoves = getMoves(player)
        drawMap(player)
        print('you are currently in room {}'.format(player))
        print('you can move {}'.format(", ".join(validMoves)))
        print('Enter QUIT to quit')

        move = input('> ')
        move = move.upper()

        if move == 'QUIT':
            print('\n See you next time! \n')
            break 
        if move in validMoves:
            player = movePlayer(player, move)
            if player == monster:
                print('\n ** Oh No!, the monster got you ! Better luck next time! ** \n')
                playing = False
            if player == door:
                print('\n ** Congrats, You have escaped ** \n')
                playing = False
        elif move not in validMoves:
            input('''\n Please enter a valid move
(Press return to continue)\n''')
        else: 
            input('''\n  Watch out for those walls, You dont want to run into them
                  (Press return to continue)
                        \n''')
    else:
        if input('Play Again? [Y/N] >').lower() != 'n':
            gameLoop()




clearScreen()
print('Welcome to the dungeon !! ')
input('Press Return to start')
gameLoop()
