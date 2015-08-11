'''
Group 2 Battleship in OOP style

classes:
y   board  - drawing, checking for placement for ships
            method to check for overlapping ships (via fleet variable_
            method to check for ship out of bounds
            
            
d   ship   -holds data for position, length, status (hit or not, on which points, sunk)
            holds data for each point and whether each point is hit.
            holds data if whole boat is sunk or not
        AircraftCarrier(ship) => [(1,2,False),(1,3,True)...]  (x_value, y_values, bool->hit or not)
        Submarine(ship)
d       PatrolBoat(ship)
        

            
            
w   player - parses input data, moves, list for guesses, list of ships
    
        self.fleet = list of ships
        __init__(self, name):
            this creates instances of the ships, and asks player to enter valid input for where to place them.
            this also creates a board for the player, and places the ships on the board
            self.loss = False
        check_fleet(self):
            if all(self.fleet.sunk == True): return LOSS
        attack(self, input):
            this input gets parsed, added to a list of guesses, and gives it to the other player to check for h,m,s
        defend(self, input):
w            this tells player to look at input and return hit, miss, or sunk.
        
            
            
y   game - watches for losses, alternates between players, etc.
        __init__(self):
            makes player instances
        check_win(player)
        
        
        def loop():
        
            while not player1.loss() AND not player2.loss():
                player1.play()
                player2.play()
                
            finishupgame()
        
        For a given turn:
            first player attacks => selects a coord from input
                                    has to be parsed
                                    passed into other player's defense method
                                        in 2p's defense method, checks against his fleet's locations
                                        keeps track of hit miss or sunk
                                        2p given option to state whether it's h, m, or s
                            game checks for win/loss
        
'''

if __name__ == '__main__':
    def game_not_over():
        if player1.fleet == sunk:
            print 'player2 is defeated.'
    attackingPlayer, defendingPlayer = defendingPlayer, attackingPlayer
    while game_not_over() == True:
        loop through game, turns
        x, y = y, x