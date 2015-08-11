import re

def draw(board):
    """"""
    print board["a1"] + " | " + board["b1"] + " | " + board["c1"]
    print "---------"
    print board["a2"] + " | " + board["b2"] + " | " + board["c2"]
    print "---------"
    print board["a3"] + " | " + board["b3"] + " | " + board["c3"]
    

def isFull(board):
    for each in board.values():
        if each == ' ':
            return False
    return True
    

def isWinner(board):
    # arrays fills in values into multi-dimensional array to test for winning conditions
    row1 = [board['a1'],board['b1'],board['c1']]
    row2 = [board['a2'],board['b2'],board['c2']]
    row3 = [board['a3'],board['b3'],board['c3']]
    if row1[0] == row1[1] == row1[2] != ' ':
        return row1[0]
    elif row2[0] == row2[1] == row2[2] != ' ':
        return row2[0]
    elif row3[0] == row3[1] == row3[2] != ' ':
        return row3[0]
    elif row1[0] == row2[0] == row3[0] != ' ':
        return row1[0]
    elif row1[1] == row2[1] == row3[1] != ' ':
        return row1[1]
    elif row1[2] == row2[2] == row3[2] != ' ':
        return row1[2]
    elif row1[0] == row2[1] == row3[2] != ' ':
        return row1[0]
    elif row3[0] == row2[1] == row1[2] != ' ':
        return row3[0]
    else:
        return False

def isTileEmpty(tile):
	if board[tile.lower()] == ' ':
		return True
	else:
		return False

def getPlayerInput(player_symbol):
    inputSuccess = False
    # REGEX for 1 of a, b, or c, and 1 of 1, 2 or 3
    validInput = re.compile(r'[a|b|c]{1}[1|2|3]{1}', re.IGNORECASE)

    while not inputSuccess:
        inp = raw_input("Please enter the move you want to make: ")
        if not validInput.match(inp):
            print "Invalid selection; please enter A, B, or C (either upper or lowercase) followed by 1, 2, or 3 (no space)."
        elif not isTileEmpty(inp):
            print "That spot is already taken."
        else:
            board[inp.lower()] = player_symbol
            inputSuccess = True

def reinit():
    for each in board.keys():
        board[each] = ' '
        
def playAgain():
    again = raw_input("Do you want to play again? (Y/N): ")
    if again.lower() == 'y':
        reinit()
        curr_player = player1
        return True
    else:
        exit('Thanks for playing!')
            

if __name__ == '__main__':
    # Board keeps track of values for the tictactoe board
    board = {'a1': ' ',
             'b1': ' ',
             'c1': ' ',
             'a2': ' ',
             'b2': ' ',
             'c2': ' ',
             'a3': ' ',
             'b3': ' ',
             'c3': ' ',
            }
    player1 = 'X'
    player2 = 'O'
    curr_player = player1
    
    running = True

    print "Welcome to Tic Tac Toe" + '\n'
    while running:
        draw(board)
        print "{} is the current player".format(curr_player)
        getPlayerInput(curr_player)
        if curr_player == player1:
            curr_player = player2
        else:
            curr_player = player1
        if isWinner(board):
            draw(board)
            print isWinner(board) + " is the winner!"
            playAgain()
        if isFull(board) == True:
            draw(board)
            print "Game Over: TIE!"
            playAgain()
