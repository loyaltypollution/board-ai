from copy import deepcopy

from game_template import GameTemplate

class Game(GameTemplate):
    playercount = 2
    def get_starting_gamestate(self):
        return {'board':[' ' for i in range(9)], 'turn':0}

    def get_legal_moves(self, gamestate = None):
        if not gamestate:
            gamestate = self.gamestate
        if self.result(gamestate) == 'pending':
            return [pos for pos, cell in enumerate(gamestate['board']) if cell == ' ']
        return []

    def project_move(self, gamestate, move):
        gamestate = deepcopy(gamestate)
        gamestate['board'][move] = gamestate['turn']
        gamestate['turn'] = int(not gamestate['turn'])
        return gamestate
    
    def get_boardstate(self, gamestate = None):
        if not gamestate:
            gamestate = self.gamestate
        gameboard = gamestate['board']
        print(gameboard[0], gameboard[1], gameboard[2])
        print(gameboard[3], gameboard[4], gameboard[5])
        print(gameboard[6], gameboard[7], gameboard[8])
    
    def result(self, gamestate = None):
        if not gamestate:
            gamestate = self.gamestate
        
        lines = [[0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [6, 4, 2]]
        for line in lines:
            if sum([gamestate['board'][index] == 0 for index in line]) == 3:
                return 'player 0 won'
            if sum([gamestate['board'][index] == 1 for index in line]) == 3:
                return 'player 1 won'
        if ' ' not in gamestate['board']:
            return 'draw'
        return 'pending'