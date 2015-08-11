


class Mode(object):
    
    def __init__(self):
        self.board = [[" " for x in range(10)] for q in range(10)] 
        self.submarine = Ship('Submarine', 3)
        self.aircraft = Ship('Aircraft', 5)
        self.patrol_boat1 = Ship('PatrolBoat1', 2)
        self.patrol_boat2 = Ship('PatrolBoat2', 2)
        #self.ships = [self.submarine, self.aircraft, self.patrol_boat1, self.patrol_boat2]
        self.ships = [self.submarine, self.aircraft]
        self.all_shots = [] 
        
    def get_array_coords(self, pos):
        d = { "ABCDEFGHIJ"[y]: str(y) for y in range(10) }
        #d= {'A': '0', 'C': '2', 'B': '1', 'E': '4'..}

        if pos[0].upper() in d.keys() and pos[1] in d.values(): 
            pos = (int(d[pos[0].upper()]), int(pos[1]))
        return pos
     
    def display_board(self):
        print "    0   1   2   3   4   5   6   7   8   9\n"
        
        current_row="A"
        for row in self.board:
            print "{:>2}".format(current_row),
            for value in row:
                print "{:^3}".format(value),
            print "\n"
            current_row = chr(ord(current_row) + 1) # A->B->C
            
    def draw_ship(self, ship):
        for coord in ship.coords:
            row = coord[0]
            col = coord[1]
            self.board[row][col] = 'O'
            
        
          
    from random import randint
    def generate_random_shot(self):
        x, y = self.randint(0,9), self.randint(0,9)
        
        if (x,y) in self.all_shots:  # if shot has been used before
            return self.generate_random_shot()
        else:
            print "Computer firing at: " + str(self.coord_to_human((x,y)))
            self.all_shots.append((x,y))
            self.check_shot((x,y))
            return (x,y)
            
    def request_user_shot(self):
        position = raw_input("Select position to fire at: ")
        array_coords = self.get_array_coords(position)
        x,y = array_coords[0], array_coords[1]
        self.all_shots.append((x,y))
        return self.check_shot((x,y))
        #return (x,y)
        
            
    def coord_to_human(self,position):
        pos_row = position[0]
        pos_col = position[1]
    
        pos_row_human = chr(ord(str(pos_row)) + 17) #convert row # to letter
        return str(pos_row_human),str(pos_col)
            
    def check_shot(self,pos):
        ship_is_hit = False
        pos_row = pos[0]
        pos_col = pos[1]
        for ship in self.ships:
            if pos in ship.coords:
                self.board[pos_row][pos_col] = "X"
                ship_is_hit = True
        if ship_is_hit == False:
            self.board[pos_row][pos_col] = "-"
        return ship_is_hit
                
    
    def game_won(self):
        game_won = 1
        for ship in self.ships:
            for coord in ship.coords:
                if coord not in self.all_shots:
                    game_won = 0
        return game_won
        
    def attack_loop(self):
        pass
     
    def defend_loop(self):
        pass
    
    def ship_sunk(self):
        #removes any ship sunk from self.ships list
        pass
    
    def game_over(self):
        #if self.ships is empty game over
        return len(self.ships) == 0
    

class Ship:
    
    def __init__(self, name, length, pos=None, orientation=None):
        self.name = name
        self.length = length
        self.position = pos #A4
        self.orientation = orientation #H
        self.coords = [] # List of (x,y) co-ords 
        self.status = {}
        
    import random
    from random import randint
    
    def computer_placement(self):
        self.position = self.randint(0,9), self.randint(0,9)
        orientation_options = ('h','v')
        self.orientation = self.random.choice(orientation_options)
        if self.check_ship_bounds():
            return self.set_coords()
        else:
            return self.computer_placement()
        
        
    
    def get_user_placement(self):
        ship_position = raw_input("Select upper left starting position: ")
        self.set_pos(ship_position)
        ship_orientation = raw_input("Select (h)orizontal or (v)ertical: ")
        self.orientation = ship_orientation
        if self.check_ship_bounds():
            return self.set_coords()  # if self.setcoords...then return it
        else:
            return self.get_user_placement()

        
    def check_ship_bounds(self):
        position_valid = True
        # check that it fits on the board
        if self.orientation.upper() == 'H':
            starting_col = self.position[1]
            if (starting_col + self.length) > 10:
                print "Sorry, ship goes off the board"
                position_valid = False
        elif self.orientation.upper() == 'V':
            starting_row = self.position[0]  
            if (starting_row + self.length) > 10:
                print "Sorry, ship goes off the board"
                position_valid = False

        return position_valid
        
    def get_array_coords(self, pos):
        d = { "ABCDEFGHIJ"[y]: str(y) for y in range(10) }
        #d= {'A': '0', 'C': '2', 'B': '1', 'E': '4'..}

        if pos[0].upper() in d.keys() and pos[1] in d.values(): 
            pos = (int(d[pos[0].upper()]), int(pos[1]))
        return pos
        
    #Converts "A2" to (0,2)
    def set_pos(self, pos):  # will set a position that will be checked, may be updated
       
        pos = self.get_array_coords(pos)
        self.position = pos 
        print pos

        
    def get_pos(self):
        return self.position
        

    def set_coords(self):
        
        row = self.position[0]
        col = self.position[1]
        
        if self.orientation.upper() == 'H':
            self.coords = [(row, col + i) for i in range(self.length)]
            
            
        elif self.orientation.upper() == 'V':
            self.coords = [(row + i, col) for i in range(self.length)]
        
            
        #if False: # there is a board collision
        #    return False
        #else: 
        #    return True
            
        
    def get_coords(self):
        return self.coords


if __name__ == "__main__":
    
    game = Mode()
    
    game_mode = raw_input("(a)ttack or (d)efend mode? ")
    
    if game_mode == 'd':
    
        for ship in game.ships:
            print "working on ship: " + str(ship.name)
            while not ship.get_user_placement():
                game.draw_ship(ship)
                game.display_board()
                break
        
        game_count = 0
        while not game.game_won():
            #if game_count > 90:
            #    break
            game.generate_random_shot()
            game.display_board()
            game_count += 1
        
        print "All ships are sunk"
    
    if game_mode == 'a':   
        
        for ship in game.ships:
            print "working on ship: " + str(ship.name)
            while not ship.computer_placement():
                #game.draw_ship(ship) #uncomment for debugging where ships are
                game.display_board()
                break
        
        game_count = 0
        while not game.game_won():
            shot_result = game.request_user_shot()
            game.display_board()
            print "Last shot hit? " + str(shot_result)
            game_count += 1
            print "shots fired: " + str(game_count)
        
        print "All ships are sunk"



# todo:  
# - simple validation on coords
# - check for ship overlap
# things I don't like:  pos_to_coord should be in separate format class
