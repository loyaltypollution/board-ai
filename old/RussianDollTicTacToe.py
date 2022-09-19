from copy import deepcopy

from game_template import GameTemplate

class Game(GameTemplate):
    playercount = 2
    
    def get_starting_gamestate(self):
        return {'board':[0 for i in range(9)], 'player0':list(range(1,6)), 'player1':list(range(1,6)), 'turn':0}
            
    def get_legal_moves(self, gamestate = None):
        if not gamestate:
            gamestate = self.gamestate

        if self.result(gamestate) != 'pending':
            return []
        
        player = 'player'+str(gamestate['turn'])
        if len(gamestate[player]) == 0:
            return []
        
        legal_moves = []
        for index, cell in enumerate(gamestate['board']):
            if abs(cell) >= max(gamestate[player]):
                continue
            if gamestate['turn'] == 0 and cell > 0:
                continue
            if gamestate['turn'] == 1 and cell < 0:
                continue
            legal_moves += [(index, value) for value in gamestate[player] if value > abs(cell)]
        return legal_moves
        
    def project_move(self, gamestate, move):
        gamestate = deepcopy(gamestate)
        index = move[0]
        value = move[1]

        assert abs(gamestate['board'][index]) < value
        player = 'player'+str(gamestate['turn'])
        assert value in gamestate[player]
        
        if player == 'player0':
            gamestate['board'][index] = value
        if player == 'player1':
            gamestate['board'][index] = -value
        
        gamestate[player].remove(value)
        gamestate['turn'] = int(not gamestate['turn'])
        return gamestate
    
    def make_move(self, move):
        self.gamestate = self.project_move(self.gamestate, move)
        self.history.append(move)
    
    def user_instructions(self):
        instructions = []
        instructions.append('index on the board')
        instructions.append('value of piece')
        return instructions
    
    def get_boardstate(self, gamestate = None):
        if not gamestate:
            gamestate = self.gamestate
        gameboard = gamestate['board']
        print(gameboard[0], '|', gameboard[1], '|' , gameboard[2])
        print(gameboard[3], '|', gameboard[4], '|' , gameboard[5])
        print(gameboard[6], '|', gameboard[7], '|' , gameboard[8])
        
        print('first  player has', gamestate['player0'])
        print('second player has', gamestate['player1'])
    
    def result(self, gamestate = None):
        if not gamestate:
            gamestate = self.gamestate
        
        gameboard = gamestate['board']
        lines = [[0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [6, 4, 2]]
        for line in lines:
            player0_checksum = [gameboard[index] > 0 for index in line]
            player1_checksum = [gameboard[index] < 0 for index in line]

            if sum(player0_checksum) == 3:
                return 'player 0 won'
            if sum(player1_checksum) == 3:
                return 'player 1 won'
        if 0 not in gamestate['board']:
            return 'draw'
        if gamestate['turn'] == 0 and len(gamestate['player0']) == 0:
            return 'draw'
        if gamestate['turn'] == 1 and len(gamestate['player1']) == 0:
            return 'draw'
        return 'pending'