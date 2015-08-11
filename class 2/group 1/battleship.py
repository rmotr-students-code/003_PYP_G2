"""
A simple battleship game in python.
Two modes: Defend and Attack.
"""

from random import randint


def clear_board(board):
    for x in range(len(board)):
        for y in range(len(board[y])):
            board[x][y] = ''

def draw_board(board):
    left = ['A','B','C','D','E','F','G','H','I','J']
    i = 0
    print "  +--0------1------2------3------4------5------6------7------8------9---+"
    for x in board:
        print left[i],
        for each in x:
            print "| ", str(each), (' '*(2-len(each))),
        print "|"
        i += 1
        print "  +---------------------------------------------------------------------+"

boats = {"Sub": 3,
         "Aircraft": 5,
         "1st patrol boat": 2,
         "2nd patrol boat": 2,}
        
        

def place_ships(board):
    global boats
    for boat in boats.keys():
        while True:
            draw_board(board)
            loc = raw_input("Enter the location (A0 through J9) of your {0}: ".format(boat))
            orientation = raw_input("Enter the orientation (H or V) of your {}: ".format(boat))
            orientation = orientation.upper()
            if parse_input(loc, orientation):
                coords = parse_input(loc, orientation)
                if boat_fits_on_board(coords, board, boat, orientation):
                    if place_boat(coords, board, boat, orientation):
                        print "Boat is placed"
                        break
                    else: continue
            else:
                print("Invalid input, Re enter the location:")
            

def boat_fits_on_board(coords, board, boat, orientation):
    global boats
    if orientation == "H":
        length = coords[1] + boats[boat]
        if length > 10:
            print "Boat out of bounds"
            return False
        else: return True
    else: #orientation.upper() == "V":
        length = coords[0] + boats[boat]
        if length > 10:
            print "Boat out of bounds"
            return False
        else: return True

def place_boat(coords, board, boat, orientation):
    global boats
    length = boats[boat]
    if orientation == 'H':
        row = coords[0]
        col = coords[1]
        for i in board[row][col:col+length]:
            if i != '':
                print "Spaces are taken! Please try another place."
                return False
        for x in range(length):
            board[row][col+x]+=boat[0]
        return True
    if orientation == 'V':
        row = coords[0]
        col = coords[1]
        #print "row: {}, col: {} len {}".format(row, col, length)
        # this makes a list of spaces that need to be blank, because you can't do vert slices
        for i in [ board[s][col] for s in range(row, row + length) ]:
            #print [ board[s][col] for s in range(row, row + length) ]
            if i:
                print "Spaces are taken! Please try another place."
                return False
        for x in range(length):
            board[row+x][col]+=boat[0]
        return True

def parse_input(loc, orientation):
    d = { "ABCDEFGHIJ"[y]: str(y) for y in range(10) }
    
    if loc[0].upper() in d.keys() and loc[1] in d.values():
        if orientation != 'H' and orientation != 'V':
            print "Invalid orientation"
            return False
        else:
            return (int(d[loc[0].upper()]), int(loc[1]))
    else:
        print "Invalid loc"
        return False


def swap_rows_and_cols(board):
    '''Rotates board by 90deg, so columns can be parsed like rows.
    Do NOT make changes using this function!'''
    board_tc = len(board) # number of rows in board
    board_tr = len(board[0]) # number of cols in board
    board_t = []
    for each in range(board_tr):
        board_t.append([])
    
    for i, j in enumerate(board): # (0, [1,2,3]), (1, [4,5,6])
        for x, y in zip(j, board_t): # pairs 1, 2, 3 with [], [], []
            y.insert(i, x)
    return board_t


def comp_fire_shots(board):
    ''' Computer fires the shots at random loacation on the board. 
        An entry is made as 'f' in that location of the board'''
    while True:
        x, y = randint(0,9), randint(0,9)
        if board[x][y].endswith('H') or board[x][y].endswith('M') or\
            ( board[x][y].endswith('S') and len(board[x][y])>1 ):
            continue
        else:
            print "Firing at {0},{1}".format(x, y)
            board[x][y] += "*"
            draw_board(board)
            if board[x][y] != '*': # if board[x][y] != ''   Check if any ship is hit?
                cell = ship_sunk(board, x, y)
                if cell != False:
                    board[x][y] = board[x][y][:-1] + 'S'
                    for a, b in cell:
                        board[a][b] = board[a][b][:-1] + 'S'
                    if is_game_over() == True:
                        print "Game Over! You Lose!"
                        draw_board(board)
                        raise SystemExit
                    return "S"   # Check if it was sunk first
                else:
                    board[x][y] = board[x][y][:-1] + 'H'
                    return "H"      #Hit  
            else:
                board[x][y] = board[x][y][:-1] + 'M'
                return "M"      #Miss
            
            
def ship_sunk(board, x, y):
    ''' If a ship is hit completely then add a 'K' to all the loc '''
    global boats
    boat = board[x][y][0]
    def parse(board, boat):
        cells = []
        for i, r in enumerate(board):
            for j, c in enumerate(r):
                if board[i][j].startswith(boat):
                    cells.append((i, j))
        return cells #--> this gives the cells in the matrix which belong to w/e boat
    cells = cells_to_check = parse(board, boat)
    cells_to_check.remove((x, y))
    for a, b in cells_to_check:
       if 'H' not in board[a][b]:
           return False
    print "Boat starting with {} is sunk!!".format(boat)
    flag = False
    name = ''
    for key in boats.keys():
        if key.startswith(boat):
            flag = True
            name = key
    if flag == True:   # can't delete boats 
        del boats[name]
        flag = False
    return cells_to_check
    
def is_game_over():
    global boats
    return len(boats) == 0

if __name__ == "__main__":
    board = [['' for x in range(10)] for x in range(10)]
    
    place_ships(board)
    while True:
        target_hit = comp_fire_shots(board)
        print "Hit(H), Miss(M) or Sunk(S)?"
        player_answer = raw_input()
        if target_hit != player_answer.upper():
            print "Dont cheat! You $%#@*& !!!\n"
        
           
        
