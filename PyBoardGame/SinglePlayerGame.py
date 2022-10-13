from copy import deepcopy

from game_template import GameTemplate

class Game(GameTemplate):
    playercount = 1    
    choices = 32
    
    def get_starting_gamestate(self):
        return {'choice':-1, 'turn':0}

    def get_legal_moves(self, gamestate = None):
        if not gamestate:
            gamestate = self.gamestate
        if self.result(gamestate) == 'pending':
            return list(range(self.choices))
        return []

    def project_move(self, gamestate, move):
        gamestate = deepcopy(gamestate)
        gamestate['choice'] = move
        return gamestate
    
    def get_boardstate(self, gamestate = None):
        if not gamestate:
            gamestate = self.gamestate
        print(gamestate['choice'])
    
    def result(self, gamestate = None):
        if not gamestate:
            gamestate = self.gamestate
        if gamestate['choice'] == -1:
            return 'pending'
        return self.evaluate(gamestate['choice'])
        
    def evaluate(self, choice):
        return choice / self.choices
    
    def get_score(self, result):
        return [result]
    
    def get_winner(self, result):
        return -1