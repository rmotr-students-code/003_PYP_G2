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
board = [[None for x in range(3)] for x in range(3)]  # 2 D array , create an empty aray ,( fill 0s for 3 rows) then repeat for the 3 cols
counter = 0


#Game function that starts and finishes game
def game():
    
    global counter
    print 'Welcome to Tic Tac Toe. Player 1 starts game.' \
          ' Input values like "A2" for Row 2 Column 2' 
   
    
    #iterates until game is won or tied
    while not won():
        display_board()
        if board_is_full() and not won():
            print 'You guys are gooood! Game Tied'
            print 'Lets start over!'
            game()

        user_input()
                    
        counter += 1
    display_board()
    if(counter%2):
        print("Player 1 WINS the game")
    else:
        print("Player 2 WINS the game")
    

def board_is_full():
    for i in range(len(board[0])):
        for j in range (len(board[0])):
            if(board[i][j] == None):
                return False
    return True
                

def user_input():
    myinput = raw_input("Enter position: ")  # A1 or B2, etc
    insert_mark(myinput)
                
def position_to_array(position):
#convert A1 -> board[0][1]
    
    position_row = position[0]
    if position_row == "A":
        row = 0
    if position_row == "B":
        row = 1
    if position_row == "C":
        row = 2

    position_col = (int) (position[1])
    if position_col>2:
        print ("Invalid column index. Should be (0:2)")
     
    return row,position_col
    
def board_value(position_row,position_col):
    return board[position_row][position_col]
    

def insert_mark(myinput):  # this should never really be used without position_open first
    position_row, position_col = position_to_array(myinput) 
    if not board_value(position_row, position_col): # is position open?
        if counter % 2 == 0:
            board[position_row][position_col] = "X"
        else: # insert with an o
            board[position_row][position_col] = "O"
    else:
        print "This position is already taken."
        user_input()
        

#displays content on board
def display_board():
    for i in range(len(board[0])):
        print board[i]


# Function that checks winning positions
def won():
    # loop through row
    # A1 B1 C1  00 01 02   board[row][col] = x ,x ,x or o,o,o
    # A2 B2 C2  10 11 12   00 01 02
    # A3 B3 C3  20 21 22   10 11 12
    if ((board[0][0] == board [0][1] == board [0][2] == "X") or #Rows
        (board[1][0] == board [1][1] == board [1][2] == "X") or
        (board[2][0] == board [2][1] == board [2][2] == "X") or
        (board[0][0] == board [0][1] == board [0][2] == "O") or
        (board[1][0] == board [1][1] == board [1][2] == "O") or
        (board[2][0] == board [2][1] == board [2][2] == "O") or
        (board[0][0] == board [1][0] == board [2][0] == "X") or  #Cols
        (board[0][1] == board [1][1] == board [2][1] == "X") or
        (board[0][2] == board [1][2] == board [2][2] == "X") or
        (board[0][0] == board [1][0] == board [2][0] == "O") or
        (board[0][1] == board [1][1] == board [2][1] == "O") or
        (board[0][2] == board [1][2] == board [2][2] == "O") or
        (board[0][0] == board [1][1] == board [2][2] == "O") or # R Diag
        (board[0][0] == board [1][1] == board [2][2] == "X") or
        (board[0][2] == board [1][1] == board [2][0] == "O") or # L Diag
        (board[0][2] == board [1][1] == board [2][0] == "X")):
           return True
        
    else:
        return False
    

game()