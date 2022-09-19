from random import choice
from pickle import dump, load
from copy import deepcopy

class PlayerTemplate:
    def load_player(self, filename=None, keys=None):
        if not filename:
            filename = type(self.game).__module__+type(self).__name__+'.pickle'

        try:
            with open(filename, 'rb') as f:
                if not keys:
                    keys = self.__dict__.keys()
                for key in keys:
                    self.__dict__[key] = deepcopy(load(f).__dict__[key])
        except:
            pass

    def register_game(self, game):
        self.game = game
    
    def save_player(self, filename=None):
        if not filename:
            filename = type(self.game).__module__+type(self).__name__+'.pickle'
        with open(filename, 'wb') as f:
            dump(self, f)

class TrueRandomAlgorithm(PlayerTemplate):
    def move(self):
        all_moves = self.game.get_legal_moves()
        self.game.make_move(choice(all_moves))

class RandomAlgorithm(PlayerTemplate):
    def move(self):
        all_moves = self.game.get_legal_moves()
        
        selected_move = choice(all_moves)
        for move in all_moves:
            projected_gamestate = self.game.project_move(self.game.gamestate, move)
            projected_result = self.game.result(projected_gamestate)
            if self.game.get_winner(projected_result) == self.game.gamestate['turn']:
                selected_move = move
                break
            enemy = int(not self.game.gamestate['turn'])
            if self.game.get_winner(projected_result) == enemy and len(all_moves) > 1:
                all_moves.remove(move)
                selected_move = choice(all_moves)
        self.game.make_move(selected_move)
        
class PlayerInterface(PlayerTemplate):
    def move(self):
        self.game.get_boardstate()
        print('all legal moves', self.game.get_legal_moves())

        instructions = self.game.user_instructions()
        if len(instructions) == 1:
            line = input('\tenter '+instructions[0]+' here: ')
            self.game.make_move(int(line))
            return 

        move = []
        for instruction in instructions:
            line = input('\tenter '+instruction+' here: ')
            move.append(int(line))
        self.game.make_move(tuple(move))