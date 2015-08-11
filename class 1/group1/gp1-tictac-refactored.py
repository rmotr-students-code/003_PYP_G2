"""
Group 1 - Tic Tac Toe

Write a simple program to play a game of Tic-Tac-Toe. The game is between two
players. The computer starts displaying the board with all the empty spots and 
asks for the first move. The computer asks each player for her move; the player 
will inform the coordinates to place her mark with a letter and a number; the 
letter indicating the column and the number the row. Example: B2 is the center 
of the board. A1 is the top left corner of the board. C3 is the bottom right 
corner (furthermost from the A1).

The computer will keep asking both player for their marks until one of them win 
or there are no more places in the board to position marks.

A1 B1 C1
A2 B2 C2
A3 B3 C3

"""


#lists to collect game input
#board = [[None,None,None],[0:3]]
board = [['' for x in range(3)] for x in range(3)]  # 2 D array , create an empty aray ,( fill Nones for 3 rows) then repeat for the 3 cols
#print board


# ---------Game function that starts and finishes game --------
def game():
    
    global counter
    
    counter = 0
    
    print 'Welcome to Tic Tac Toe. Player 1 starts game.' \
          ' Input values like "B2" for Row 2 Column 2 or ' \
          '"C1" for Row 1 Column 3. Good Luck!'

    
    display_board()
    
    #while loop that iterates until game is won or tied
    #global counter = 0
    while not won():

        if board_is_full() and not won():
            print 'You guys are good! Game Tied.'
            break
        
        user_input()
        
        display_board()
        
        if won():
            if counter % 2 == 1:
                print "Player 1 Wins"
            else:
                print "Player 2 Wins"
    
        
# -------------------- main game loop above ------------------            
  
def user_input():
    if counter % 2 == 0:
        myinput = raw_input("Player 1 (X), Enter position to add mark: ")
    else:
        myinput = raw_input("Player 2 (O), Enter position to add mark: ")
        
    input_whitelist = ['A1','a1','A2','a2','A3','a3','B1','b1','B2','b2','B3','b3','C1','c1','C2','c2','C3','c3']
    # could simplify to regex or lower()
    if myinput in input_whitelist:
        insert_mark(myinput)
    else:
        print"Invalid input, please use the format A1, B2, C3, etc"
        user_input()
        
def position_to_tuple(position): # convert A1 to 01, B2 to 22, etc
    if position[0].lower() == 'a':
        position_row = 0
    if position[0].lower() == 'b':
        position_row = 1
    if position[0].lower() == 'c':
        position_row = 2
    
    position_col = int(position[1]) - 1 
    
    return int(position_row), int(position_col) # returns needed array indexes as a tuple

def position_value(position):
    position_row, position_col = position_to_tuple(position)
    return board[position_row][position_col]

def insert_mark(position):  
    global counter
    position_row, position_col = position_to_tuple(position)
    if position_value(position) == '':    # make sure space isn't used yet
        if counter % 2 == 0:
            board[position_row][position_col] = "X"
            counter += 1
        else: 
            board[position_row][position_col] = "O"
            counter += 1
    else:
        print "Sorry, that position is already taken."
        user_input()
        

#displays content on board
def display_board():
        print '\t1\t2\t3\n'
        print 'A\t' + str(board[0][0]) + '\t' + str(board[0][1]) + '\t' + str(board[0][2]) + '\n'
        print 'B\t' + str(board[1][0]) + '\t' + str(board[1][1]) + '\t' + str(board[1][2]) + '\n'
        print 'C\t' + str(board[2][0]) + '\t' + str(board[2][1]) + '\t' + str(board[2][2]) + '\n'
        print '\n'


# Function that checks winning positions
def won():
    
#    A1 B1 C1  00 01 02
#    A2 B2 C2  10 11 12
#    A3 B3 C3  20 21 22
    return  board[0][0] == board[0][1] == board[0][2] == 'X' or \
            board[1][0] == board[1][1] == board[1][2] == 'X' or \
            board[2][0] == board[2][1] == board[2][2] == 'X' or \
            board[0][0] == board[0][1] == board[0][2] == 'O' or \
            board[1][0] == board[1][1] == board[1][2] == 'O' or \
            board[2][0] == board[2][1] == board[2][2] == 'O' or \
            board[0][0] == board[1][0] == board[2][0] == 'X' or \
            board[0][0] == board[1][0] == board[2][0] == 'O' or \
            board[0][1] == board[1][1] == board[2][1] == 'X' or \
            board[0][1] == board[1][1] == board[2][1] == 'O' or \
            board[0][2] == board[1][2] == board[2][2] == 'X' or \
            board[0][2] == board[1][2] == board[2][2] == 'O' or \
            board[0][0] == board[1][1] == board[2][2] == 'X' or \
            board[0][0] == board[1][1] == board[2][2] == 'O' or \
            board[0][2] == board[1][1] == board[2][0] == 'X' or \
            board[0][2] == board[1][1] == board[2][0] == 'O'
    
    
    # if board[0][0] == board[0][1] == board[0][2] == 'X' or \
    #     board[1][0] == board[1][1] == board[1][2] == 'X' or \
    #     board[2][0] == board[2][1] == board[2][2] == 'X' or \
    #     board[0][0] == board[0][1] == board[0][2] == 'O' or \
    #     board[1][0] == board[1][1] == board[1][2] == 'O' or \
    #     board[2][0] == board[2][1] == board[2][2] == 'O' or \
    #     board[0][0] == board[1][1] == board[2][2] == 'X' or \
    #     board[0][2] == board[1][1] == board[2][0] == 'O':
        
    #     return True


#checks if board is full
def board_is_full():
    return counter == 9

game()