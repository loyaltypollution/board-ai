from BasicAlgorithms import PlayerTemplate
from Heuristic import Heuristic

class MinimaxAlgorithm(PlayerTemplate):
    def __init__(self, depth, heuristic, filename=None):
        self.depth = depth
        self.heuristic = heuristic
        self.filename = filename

    def register_game(self, game):
        self.game = game
        self.load_player(self.filename, ['heuristic'])
        
    def move(self):        
        def dfs(gamestate, depth, alpha, prev_turn):
            all_moves = self.game.get_legal_moves(gamestate)
            if depth == 0 or len(all_moves) == 0:
                return self.heuristic.evaluate(gamestate)
            
            best_outcome = [0, 0]
            best_move  = None
            for move in all_moves:
                projected_gamestate = self.game.project_move(gamestate, move)
                projected_evaluation_outcome = dfs(projected_gamestate, depth - 1, best_outcome, gamestate['turn'])
                if projected_evaluation_outcome[gamestate['turn']] > best_outcome[gamestate['turn']] or not best_move:
                    best_outcome = projected_evaluation_outcome
                    best_move = move
                if alpha[prev_turn] < best_outcome[prev_turn]:
                    break
            if depth == self.depth:
                return best_move
            return best_outcome
        
        best_move = dfs(self.game.gamestate, self.depth, [0,0], self.game.gamestate['turn'])
        self.game.make_move(best_move)
