from ship import *
from board import *

"""
Player class. Parses input data, Create ships and board for respective player 
"""
class Player(object):
    
    ''' Constructor'''
    def __init__(self,name):
        self.name = name
        self.loss = False
        
        #create empty fleet
        self.fleet = []
        
        #create instance of board
        self.board = Board()

    
    ''' 
    Asks player for ship positions and orientation
    Will fill the fleet with ships after each inserted position and orientation
    '''
    def askPositions(self):
        ship_names = ["Aircraft Carrier", "Battleship", "Cruiser", "Submarine", "Destroyer"]
        vertical = False
        print "********** " + self.name + " **********"
        for shipname in ship_names:
            #asks player for starting ship coordinate
            while True:
                try:
                    position = raw_input("Give a starting coordinate for your " + shipname + ". Format: (x,y)\n")
                    if len(position) < 3:
                        print "\nOops! Wrong format. Try again."
                        continue
                    
                    #TODO: Need to check board if the coordinate already exists
                    
                    positionTuple = (int(position[1]), int(position[3]))
                    break
                except ValueError:
                    print "\nOops! Wrong format. Try again."
                    
            #asks player for orientation        
            while True:
                orientation = raw_input("Select the orientation. Horizontal or Vertical?\n")
                if orientation.lower() != "horizontal" and orientation.lower() != "vertical":
                    print "\nOops! Wrong format. Please type Horizontal or Vertical."
                    continue
                if orientation.lower() == "vertical":
                    vertical = True
                break
            
            #creates instance of ship and inserts into fleet
            s = Ship(positionTuple, vertical, shipname)
            self.fleet.append(s)
            
    
    ''' returns true if entire fleet is sunk '''        
    def fleetSunk(self):
        #check if players fleet is sunk.
        for ship in self.fleet:
            if ship.sunk() == False:
                return False
        return True
    
    
    def attack(self):
        print "\n*** " + self.name + " ***"
        #asks for attacking move
        while True:
                try:
                    position = raw_input("Give a coordinate you wish to attack. Format: (x,y)\n")
                    if len(position) < 3:
                        print "\nOops! Wrong format. Try again."
                        continue
                    positionTuple = (int(position[1]), int(position[3]))
                    break
                except ValueError:
                    print "\nOops! Wrong format. Try again."
        return positionTuple
        
    
    def defend(self, shot):
        #take in attack from other player
        for ship in fleet:
            if ship.attack(shot):
                print "Hit!"
                
                if ship.sunk():
                    print self.name + "\'s " +  ship.name + " has sunk!"
                    
                if self.fleetSunk():
                    self.loss = True
                #update board somehow
            else:
                print "Miss!"
                #update board somehow


#test
p = Player("Player 1")
p.askPositions()
p.attack()
