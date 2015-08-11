"""
Defend mode:
- place ships (1) 3 (1) 5 (2) 2
- horizontal or vertical
- must check bounds of board
- must check for overlapping ships

will receive random attacks
prompt after fire if hit or miss
(check for truth)
no repeat fires
EC: more than random targeting

Board: A-J and 1-10 for columns

00 01 02 03 04 05...
10
20
30
40
50

"""

import random

shots_fired = 0
board = [[" " for x in range(10)] for q in range(10)]  # 2 D array , create an empty aray ,( fill Nones for 3 rows) then repeat for the 3 cols


# how are we going to store all the ships on the board
    

def draw_board():
    #draw board with formatting

    print "    0   1   2   3   4   5   6   7   8   9\n"
        
    current_row="A"
    for row in board:
        print "{:>2}".format(current_row),
        for value in row:
            print "{:^3}".format(value),
        print "\n"
        current_row = chr(ord(current_row) + 1) # A->B->C
            
already_called = []
ships = {"aircraft":[],"submarine":[]}  #update_board[x][y]
ship_lengths = {"aircraft":5, "submarine":3}


def place_ships():  
    global ships
    global ship_lengths
    for ship_key,ship_length in ship_lengths.items():  # cycle through all ships to place
        ship_start_position = raw_input("Please select upper left position for "+str(ship_key)+": ")
        ship_orientation = raw_input("(H)orizontal or (V)ertical: ")
        
        # convert user friendly text to 2D array indices
        position = position_to_tuple(ship_start_position)
        position_row, position_col = position
    
        if is_position_valid(position,ship_orientation,ship_length):
            if ship_orientation == 'H':
                for extend_ship in range(0,ship_length):
                    newposition =  tuple((position_row,position_col+extend_ship))
                    board[position_row][position_col+extend_ship] = 'O'
                    ships[ship_key].append(newposition)
            elif ship_orientation == 'V':
                for extend_ship in range(0,ship_length):
                    newposition =  tuple((position_row+extend_ship,position_col))
                    board[position_row+extend_ship][position_col] = 'O'
                    ships[ship_key].append(newposition)
        else:
            break
                
        

def is_position_valid(starting_position,ship_orientation,ship_length):
    
    position_valid = True
    # check that it fits on the board
    if ship_orientation == 'H':
        starting_col = starting_position[1]
        if (starting_col + ship_length) > 9:
            print "Sorry, ship goes off the board"
            position_valid = False
    elif ship_orientation == 'V':
        starting_row = starting_position[0]
        if (starting_row + ship_length) > 9:
            print "Sorry, ship goes off the board"
            position_valid = False
    
    # check for no overlap with other ships
    # Generate all tuples for this ship, then loop through all other ships
    # position_valid = False
        
    return position_valid
        
    
def generate_random_shot():
    guessrow = random.randint(0, 9)
    guesscol = random.randint(0, 9)
    if (guessrow,guesscol) in already_called:
        return generate_random_shot()
    else:
        return guessrow,guesscol

def check_shot(position): 
    global ships
    global shots_fired
    position_tuple = position
    
    shots_fired += 1
    
    if position_tuple in already_called:
        return False
    
    # see if it's a hit or not - check the ship dictionaries?
    is_hit = False
    print ships
    print position_tuple
    for ship_name,ship_positions in ships.iteritems():
        if position_tuple in ship_positions:
            #hit
            #update board
            board[position_tuple[0]][position_tuple[1]] = 'X'
            #now clear from ships dictionary
            ships[ship_name].remove(position_tuple)
            #add position to list of already called positions
            already_called.append(position_tuple)
            is_hit = True
            return "hit"
    
    if is_hit == False:
        board[position_tuple[0]][position_tuple[1]] = '-'
        already_called.append(position_tuple) 
    
    return "miss"
                    
    


#board[0][1] = X
#ships[ship1].remove(1,2) #< delete tuple from ship to indicate a hit
# hit OR miss put tuple in already_called list

    
def position_to_tuple(position): # convert A1 to 01, B2 to 22, etc
    if position[0].lower() == 'a':
        position_row = 0
    if position[0].lower() == 'b':
        position_row = 1
    if position[0].lower() == 'c':
        position_row = 2
    if position[0].lower() == 'd':
        position_row = 3
    if position[0].lower() == 'e':
        position_row = 4
    if position[0].lower() == 'f':
        position_row = 5
    if position[0].lower() == 'g':
        position_row = 6
    if position[0].lower() == 'h':
        position_row = 7
    if position[0].lower() == 'i':
        position_row = 8
    if position[0].lower() == 'j':
        position_row = 9
    
    position_col = int(position[1]) 
    return int(position_row), int(position_col) # returns needed array indexes as a tuple
    
    #(0,1)
    #row = postiion[0] 
    #col = position[1]
    #board[row][col] = "X"
    
def position_to_human(position):
    pos_row = position[0]
    pos_col = position[1]
    
    pos_row_human = chr(ord(str(pos_row)) + 17) #convert row # to letter
    return str(pos_row_human),str(pos_col)
    

def select_mode():
    game_mode = raw_input("(D)efend or (A)ttack: ")
    
    return game_mode


def game_won():
    for ship, ship_positions in ships.iteritems():
        if len(ship_positions) > 0:
            return False
    return True
      
if __name__ == "__main__":


    position_to_human((3,5))
    #game_mode = select_mode();
    game_mode = 'D'
    
    if game_mode == 'D':

        draw_board()
        place_ships()
        
        while not game_won():
            random_position = generate_random_shot()
            # remember to avoid duplicate positions - updated random
            print "Computer firing at: "+ str(position_to_human(random_position))
            shot_result =  check_shot(random_position)
            
            #my_feedback = raw_input("Computer: Was my shot a (H)it or (M)iss? ")
            #if (shot_result == "hit" and my_feedback == "H") or (shot_result == "miss" and my_feedback == "M"):
            #    print "Correct, it was a "+str(shot_result)
            #else:
            #    print "Liar! It was a "+str(shot_result)
            
            draw_board()
            
            if shots_fired > 100:
                break
        
        if game_won():
            print "all ships sunk"
        
        draw_board()
        
        print "number of computer shots fired: "+ str(shots_fired)
        #print already_called
        
        
                
        
        
    elif game_mode == 'A':
        pass
   
    
    
    
