import random

# The following function prints the current board to the command window.
def print_board(board):
    print()
    print(board[:3])
    print(board[3:6])
    print(board[6:])
    print()
    
# This function takes the existing board, position input from player,
# marker type (either x or o) and returns the updated board based on the arguments.
def update_board(board, position, marker):
    board[position-1] = marker
    print_board(board)
    return board

# Functions for executing player 1's and 2's moves.
def player_1():
    marker = "x"
    while True:

        position = int(input("What position would you like to place your piece?: ")) # Takes input from user.
        if board[position - 1] != " " or position not in range(1,10): # Validates position.
            print("Invalid position, try again.")
        else:
            update_board(board, position, marker) # Updates board.
            return False
    
def player_2():
    marker = "o"
    while True:
        position = int(input("What position would you like to place your piece?: "))
        if board[position - 1] != " " or position not in range(1,10):
            print("Invalid position, try again.")
        else:
            update_board(board, position, marker)
            return False

# Function for executing the computers moves.
def computer():
    marker = "o"
    while True:
        position = random.randint(1,9) # Imports random integer 1-9 as the position.
        if board[position - 1] != " ": # Validates position.
            print("Invalid position, try again.")
        else:
            update_board(board, position, marker)
            return False

# Below are all the functions used to determine the state of the game.

# Checks all possible wins for x and o.
def win_x():
    if board[0] == board[1] == board[2] =="x":
        return True
    elif board[3] == board[4] == board[5] =="x":
        return True
    elif board[6] == board[7] == board[8] =="x":
        return True
    elif board[0] == board[3] == board[6] =="x":
        return True
    elif board[1] == board[4] == board[7] =="x":
        return True
    elif board[2] == board[5] == board[8] =="x":
        return True
    elif board[0] == board[4] == board[8] =="x":
        return True
    elif board[2] == board[4] == board[6] =="x":
        return True
    else:
        False

def win_o():
    if board[0] == board[1] == board[2] =="o":
        return True
    elif board[3] == board[4] == board[5] =="o":
        return True
    elif board[6] == board[7] == board[8] =="o":
        return True
    elif board[0] == board[3] == board[6] =="o":
        return True
    elif board[1] == board[4] == board[7] =="o":
        return True
    elif board[2] == board[5] == board[8] =="o":
        return True
    elif board[0] == board[4] == board[8] =="o":
        return True
    elif board[2] == board[4] == board[6] =="o":
        return True
    else:
        False

# Combines both win functions and displays a congratulatory message to the winner if one is True.
def check_win():
    if win_x() == True:
        print("Congratulations player 1! You have won!")
        return True
    elif win_o() == True:
        print("Congratulations player 2! You have won!")
        return True
    else:
        return False
        
# This function is used to check for a draw if there is no win. 
# Checks if there are no more free spaces on the board, if True informs users there's a draw.
def draw():
    if " " not in board:
        print("It's a draw.")
        return True
    else:
        return False

# Function used to continue the game if there is neither a win or a draw.
def no_outcome():
    print("Next move :)")

# This function combines the 3 states and checks for them in a specific order.
def state():
    if check_win() == True: # Checks for a win.
        print("Thank you for playing :)")
        return True
    else:
        if draw() == True: # Checks for a draw.
            print("Thank you for playing :)")
            return True
        else:
            no_outcome() # If neither of the above are true, continues the game.
            return False

# Functions for the 2 different game modes.
# Mode 1 = PvP and Mode 2 = PvC

def mode_1():
    while True:
        print("*Player 1's turn*")
        player_1()
        if state() == True:
            break
        print("*Player 2's turn*")
        player_2()
        if state() == True:
            break

def mode_2():
    while True:
        print("*Player 1's turn*")
        player_1()
        if state() == True:
            break
        print("*Player 2's turn*")
        computer()
        if state() == True:
            break

# Main program below

board = [" "," "," "," "," "," "," "," "," "]
position = ['1','2','3','4','5','6','7','8','9']
print_board(board)
print("The board below shows the positions.")
print_board(position)

# Asks user to select a game mode.
print("Player vs Player = mode 1")
print("Player vs Computer = mode 2")
print()

# Exception handling to make sure the user inputs an integer that is either 1 or 2.
while True:
    try:
        mode = int(input("Please select a game mode (1 or 2): "))
        if mode in range(1,3):
            break
        else:
            print("Out of range, try again...")
    except ValueError:
        print("Invalid input, please enter a valid game mode...")
print()
print("Successfully entered game mode", mode)

# Executes the function for either of the game modes depending on the users choice.

if mode == 1:
    print()
    print("Player 1 will begin as X, followed by player 2 as O.")
    print()
    mode_1()
    exit()

elif mode == 2:
    print()
    print("Player 1 (human) will begin as X, followed by player 2 (computer) as O.")
    print()
    mode_2()
    exit()

    
