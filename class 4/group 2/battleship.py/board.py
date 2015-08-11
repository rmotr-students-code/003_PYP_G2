'''
This is the board class. Each player gets a board object instantiated.
The board reads the player's fleet attribute, and places the ships/values accordingly when drawing the board.
The board also has a method to keep track of the opposing player's guesses.
'''

class Board(object):
    '''
    This is the board class. Each player gets a board object instantiated.
    The board reads the player's fleet attribute, and places the ships/values accordingly when drawing the board.
    The board also has a method to keep track of the opposing player's guesses.
    '''
    
    def __init__(self):
        self.grid = [[' ' for _ in range(10)] for _ in range(10)]
        self.defend_misses = [] # keep track of misses when other player attacks
        self.attack_misses = [] # keep track of misses when you attack other player
        
    def check_placement(self, x, y, player):
        '''
        This checks if the placement is out of bounds or if the boat is already on
        the board somewhere. Need to call this method with the player whose board it is,
        so it can access the player's fleet attribute.
        '''
        if 0 <= x <= 9 and 0 <= y <= 9:
            break #continue with checking
        else:
            return False
        coords = (x, y)
        
    
    def draw_board_attack(self):
        '''
        This draws the board for attack purposes. It will show hits on enemy ships,
        misses, and sunken ships.
        '''
        left = ['0','1','2','3','4','5','6','7','8','9']
        i = 0
        print "  +--0------1------2------3------4------5------6------7------8------9---+"
        for x in self.grid:
            print left[i],
            for each in x:
                print "| ", str(each), (' '*(2-len(each))),
            print "|"
            i += 1
            print "  +---------------------------------------------------------------------+"
            
        
    def draw_board_defend(self):
        '''
        This draws the board for defense purposes. It shows the status of one's own
        ships. It shows hits, misses, sunken ships, and the position of the ships.
        '''
        left = ['0','1','2','3','4','5','6','7','8','9']
        i = 0
        print "  +--0------1------2------3------4------5------6------7------8------9---+"
        for x in self.grid:
            print left[i],
            for each in x:
                print "| ", str(each), (' '*(2-len(each))),
            print "|"
            i += 1
            print "  +---------------------------------------------------------------------+"
        
    def swap_rows_and_cols(self):
        '''transposes rows and columns, so columns can be parsed like rows.
        Do NOT make changes using this function!'''
        board_tc = len(self.board) # number of rows in board
        board_tr = len(self.board[0]) # number of cols in board
        board_t = []
        for each in range(board_tr):
            board_t.append([])
        
        for i, j in enumerate(board): # (0, [1,2,3]), (1, [4,5,6])
            for x, y in zip(j, board_t): # pairs 1, 2, 3 with [], [], []
                y.insert(i, x)
        return board_t