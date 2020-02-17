# This is a simple Rock Paper Scissors game that saves your score.
# It demonstrates defining functions and using them, importing modules,
# using standard library functions, control flow, a do while loop,
# taking inputs, and printing results
import random
import sys


#This method randomizes the computer's move, returns the move as a string
def computer():
    global comp
    turn = True

    while turn:
        comp_shoot = random.randint(1, 4)
        if comp_shoot == 1:
            comp = 'rock'
            return comp
        elif comp_shoot == 2:
            comp = 'scissors'
            return comp
        elif comp_shoot == 3:
            comp = 'paper'
            return comp
        elif comp_shoot == 'None':
            continue

#Comparing the player's input and the computer's
def playround():
    global comwins
    global playerwins

    if comp == player_input:
        print('Draw!')
    elif comp == 'rock' and player_input == 'scissors':
        print('computer wins!')
        comwins = comwins + 1
    elif comp == 'rock' and player_input == 'paper':
        print('player wins!')
        playerwins = playerwins + 1
    elif comp == 'scissors' and player_input == 'paper':
        print('computer wins!')
        comwins = comwins + 1
    elif comp == 'scissors' and player_input == 'rock':
        print('player wins!')
        playerwins = playerwins + 1
    elif comp == 'paper' and player_input == 'rock':
        print('computer wins!')
        comwins = comwins + 1
    elif comp == 'paper' and player_input == 'scissors':
        print('player wins!')
        playerwins = playerwins + 1
    elif player_input == 'rock' and comp == 'scissors':
        print('player wins!')
        playerwins = playerwins + 1
    elif player_input == 'rock' and comp == 'paper':
        print('computer wins!')
        comwins = comwins + 1
    elif player_input == 'scissors' and comp == 'paper':
        print('player wins!')
        playerwins = playerwins + 1
    elif player_input == 'scissors' and comp == 'rock':
        print('computer wins!')
        comwins = comwins + 1
    elif player_input == 'paper' and comp == 'rock':
        print('player wins!')
        playerwins = playerwins + 1
    elif player_input == 'paper' and comp == 'scissors':
        print('computer wins!')
        comwins = comwins + 1

#Default parameters/variables
playgame = True
comwins = 0
playerwins = 0

#The main code for the game lives in a do while loop
while playgame:
    print()
    print('Rock Paper Scissors...Shoot!')
    raw_input = input()
    # Makes sure the input isn't case sensitive
    player_input = raw_input.lower()
    comp = computer()
    print('Computer played: ' + str(comp))
    print()

    playround()

    print('You have: ' + str(playerwins) + ' wins')
    print('Computer has: ' + str(comwins) + ' wins')
    print()

    print('Would you like to play another round? Y or N')
    playagain = input()
    if playagain == 'Y' or playagain == 'y':
        continue
    else:
        print('Thanks for playing!')
        break

sys.exit()
