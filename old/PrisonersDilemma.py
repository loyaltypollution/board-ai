from copy import deepcopy

from game_template import GameTemplate

class Game(GameTemplate):
    playercount = 2
    payout_matrix = [[(-5,-5),(0,-10)],[(-10,0),(-1,-1)]]
 
    def get_starting_gamestate(self):
        return {'player0':-1, 'player1':-1, 'turn':0}
                
    def get_legal_moves(self, gamestate = None):
        if not gamestate:
            gamestate = self.gamestate
        player = 'player'+str(gamestate['turn'])
        if gamestate[player] == -1:
            return list(range(len(self.payout_matrix)))
        return []
        
    def project_move(self, gamestate, move):
        gamestate = deepcopy(gamestate)
        player = 'player'+str(gamestate['turn'])
        gamestate[player] = move
        gamestate['turn'] = int(not gamestate['turn'])
        return gamestate
    
    def make_move(self, move):
        self.gamestate = self.project_move(self.gamestate, move)
        self.history.append(move)
        
    def get_boardstate(self, gamestate = None):
        if not gamestate:
            gamestate = self.gamestate
        print(gamestate['player0'])
        print(gamestate['player1'])
    
    def result(self, gamestate = None):
        if not gamestate:
            gamestate = self.gamestate
        
        if gamestate['player0'] == -1 or gamestate['player1'] == -1:
            return 'pending'

        outcome = self.payout_matrix[gamestate['player0']][gamestate['player1']]
        return outcome
     
    def get_score(self, result):
        '''given an outcome of the game, reports score differential.'''
        if result == 'pending':
            return [0,0]
        def recursive_map(f, arr):
            if isinstance(arr, list) or isinstance(arr, tuple):
                return f([recursive_map(f,i) for i in arr])
            return arr
        # normalise outcome table to the range (0,1) inclusive
        largest  = recursive_map(max, self.payout_matrix)
        smallest = recursive_map(min, self.payout_matrix)
        return [(i-smallest)/(largest-smallest) for i in result]