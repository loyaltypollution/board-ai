from copy import deepcopy

from game_template import GameTemplate

class Game(GameTemplate):
    playercount = 2    
    def get_starting_gamestate(self):
        return {'board':[' ' for i in range(81)], 'meta_index':-1, 'meta':[' ' for i in range(9)],'turn':0}
    
    def get_legal_moves(self, gamestate = None):
        if not gamestate:
            gamestate = self.gamestate
        
        gameboard = gamestate['board']
        gamemeta = gamestate['meta']
        gamemeta_index = gamestate['meta_index']
        
        open_board = [pos for pos, cell in enumerate(gameboard) if cell == ' ' and gamemeta[int(pos/9)] == ' ']
        if gamestate['meta_index'] == -1:
            return open_board

        gameregion = gameboard[9*gamemeta_index:9*gamemeta_index+9]
        return  [9*gamemeta_index+pos for pos, cell in enumerate(gameregion) if cell == ' ']
        
        return open_board
    
    def project_move(self, gamestate, move):
        gamestate = deepcopy(gamestate)
        gameboard = gamestate['board']
        gameturn  = gamestate['turn']

        assert gameboard[move] == ' '
        assert gamestate['meta_index']  == int(move/9) or gamestate['meta_index'] == -1

        gameboard[move] = gameturn
        gamestate['meta_index'] = move % 9
        if gamestate['meta'][gamestate['meta_index']] != ' ':
            gamestate['meta_index'] = -1
        if ' ' not in gameboard[9*gamestate['meta_index']:9*gamestate['meta_index']+9]:
            gamestate['meta_index'] = -1
            
        lines = [[0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [6, 4, 2]]
        for line in lines:
            if sum([gameboard[move-move%9+cell] == gameturn for cell in line]) == 3:
                gamestate['meta'][int(move/9)] = gameturn
                break

        gamestate['turn'] = int(not gameturn)
        return gamestate
        
    def get_boardstate(self, gamestate = None):
        if not gamestate:
            gamestate = self.gamestate
        row_indexes = [0,1,2,9,10,11,18,19,20]
        offsets = [0,3,6,-1,27,30,33,-1,54,57,60]
        for offset in offsets:
            if offset == -1:
                print(21*'-')
                continue
            row = [str(gamestate['board'][index+offset]) for index in row_indexes]
            row.insert(6,'|')
            row.insert(3,'|')
            print(' '.join(row))
        
        gamemeta = gamestate['meta']
        print('macro boardstate: ')
        print(gamemeta[0], gamemeta[1], gamemeta[2])
        print(gamemeta[3], gamemeta[4], gamemeta[5])
        print(gamemeta[6], gamemeta[7], gamemeta[8])
    
    def result(self, gamestate = None):
        if not gamestate:
            gamestate = self.gamestate
        
        gamemeta = gamestate['meta']
        
        lines = [[0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [6, 4, 2]]
        for line in lines:
            if sum([gamemeta[cell] == 0 for cell in line]) == 3:
                return 'player 0 won'
            if sum([gamemeta[cell] == 1 for cell in line]) == 3:
                return 'player 1 won'
        if ' ' not in gamemeta:
            return 'draw'
        if not self.get_legal_moves():
            enemy = int(not self.gamestate['turn'])
            return 'player '+str(enemy)+' won'
        return 'pending'