from copy import deepcopy

from game_template import GameTemplate

class Game(GameTemplate):
    playercount = 2
    def get_starting_gamestate(self):
        return {'board':[' ' for i in range(27)], 'turn':0}
                
    def get_legal_moves(self, gamestate = None):
        if not gamestate:
            gamestate = self.gamestate
        return [i for i in range(9) if gamestate['board'][i+18] == ' ']
        
    def project_move(self, gamestate, move):
        gamestate = deepcopy(gamestate)
        column = [gamestate['turn']] + [gamestate['board'][move + i] for i in range(0, 18, 9)]
        
        for i in range(3):
            gamestate['board'][move+9*i] = column[i]
        gamestate['turn'] = int(not gamestate['turn'])
        return gamestate
    
    def make_move(self, move):
        self.gamestate = self.project_move(self.gamestate, move)
        self.history.append(move)
        
    def get_boardstate(self, gamestate = None):
        if not gamestate:
            gamestate = self.gamestate
        gameboard = gamestate['board']
        for i in range(0,27,9):
            print(gameboard[0+i], '|', gameboard[1+i], '|' , gameboard[2+i])
            print(gameboard[3+i], '|', gameboard[4+i], '|' , gameboard[5+i])
            print(gameboard[6+i], '|', gameboard[7+i], '|' , gameboard[8+i])
            print()
    
    def result(self, gamestate = None):
        if not gamestate:
            gamestate = self.gamestate
        
        gameboard = gamestate['board']
        lines = [[0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [6, 4, 2], [9, 10, 11], [12, 13, 14], [15, 16, 17], [9, 12, 15], [10, 13, 16], [11, 14, 17], [9, 13, 17], [15, 13, 11], [18, 19, 20], [21, 22, 23], [24, 25, 26], [18, 21, 24], [19, 22, 25], [20, 23, 26], [18, 22, 26], [24, 22, 20], [0, 13, 26], [2, 13, 24], [1, 13, 25], [3, 13, 23], [4, 13, 22], [5, 13, 21], [6, 13, 20], [7, 13, 19], [8, 13, 18], [0, 9, 18], [1, 10, 19], [2, 11, 20], [3, 12, 21], [5, 14, 23], [6, 15, 24], [7, 16, 25], [8, 17, 26], [0, 10, 20], [2, 10, 18], [0, 12, 24], [6, 12, 18], [2, 14, 26], [8, 14, 20], [6, 16, 26], [8, 16, 24]]
        for line in lines:
            player0_checksum = [gameboard[index] == 0 for index in line]
            player1_checksum = [gameboard[index] == 1 for index in line]

            if sum(player0_checksum) == 3:
                return 'player 0 won'
            if sum(player1_checksum) == 3:
                return 'player 1 won'
        if ' ' not in gamestate['board']:
            return 'draw'
        return 'pending'
    def game_start(self, hide = False):        
        while self.result() == 'pending':
            turn = self.gamestate['turn']
            self.players[turn].move()
        if not hide:
            self.get_boardstate()
        return self.result()