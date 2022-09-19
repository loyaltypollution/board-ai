from math import sqrt, log
from copy import deepcopy

from BasicAlgorithms import PlayerTemplate, RandomAlgorithm

class MonteCarloAlgorithm(PlayerTemplate):

    class Node:
        def __init__(self, parent, move = None, algorithm = None):
            self.parent = parent
            self.children = {}
            self.t = []
            self.n = 0
            self.move = move

            if parent and not algorithm:
                self.algorithm = parent.algorithm
                self.turn = int(not parent.turn)
                return
            self.algorithm = algorithm
            self.turn = 1
        
        def get_gamestate(self):
            def upward_traversal(node):
                if node == node.algorithm.root:
                    return node.algorithm.game.get_starting_gamestate()
                return node.algorithm.game.project_move(upward_traversal(node.parent), node.move)
            return upward_traversal(self)
        
        def expand(self):
            if self.children:
                return
            gamestate = self.get_gamestate()
            possible_moves = self.algorithm.game.get_legal_moves(gamestate)
            self.children = {move:MonteCarloAlgorithm.Node(self, move = move) for move in possible_moves}
        
        def select(self):            
            if self.n == 0:
                score = self.path()
                self.n += 1
                self.t = score
                return score
            
            self.expand()
            if not self.children:
                return [0 for i in range(len(self.algorithm.game.players))]

            def ucb_value(child):
                if child.n == 0:
                    return 999999
                exploitation = child.t[self.algorithm.gamestate['turn']] / child.n
                exploration = 1.41 * sqrt(log(self.algorithm.pointer.n) / child.n)
                return exploitation + exploration
            values = [ucb_value(child) for child in self.children.values()]
            selected_node_index = values.index(max(values))
            selected_node = list(self.children.values())[selected_node_index]
            score = selected_node.select()
            self.n += 1
            self.t = [self.t[i] + score[i] for i in range(len(score))]
            return score
        
        def path(self):
            players = [RandomAlgorithm() for i in range(self.algorithm.game.playercount)]
            simulated_game = type(self.algorithm.game)(*players)
            simulated_game.gamestate = deepcopy(self.get_gamestate())
            result = simulated_game.game_start(True)

            return simulated_game.get_score(result)
        
        def check_states(self, depth, maxdepth=None):
            if not maxdepth:
                maxdepth = depth
            print((maxdepth-depth) * '   ', self.t, self.n, self.move)
            if depth == 0 or not self.children:
                return
            for child in self.children.values():
                child.check_states(depth - 1, maxdepth)
    
    
    def __init__(self, depth, filename=None):
        self.root = MonteCarloAlgorithm.Node(None, algorithm = self)
        self.pointer = self.root
        self.depth = depth
        self.filename = filename
        
    def register_game(self, game):
        self.game = game        
        self.gamestate = game.gamestate

        self.load_player(self.filename, ['root'])
        self.pointer = self.root
        
    def update_history(self):
        self.pointer = self.root
        for move in self.game.history:
            self.pointer.expand()
            self.pointer = self.pointer.children[move]
        self.gamestate = self.game.gamestate
            
    def move(self):
        self.update_history()
        self.pointer.expand()
        for i in range(self.depth):
            self.pointer.select()
                
        possible_moves = [(child.t[self.gamestate['turn']] / child.n, child.move) for child in self.pointer.children.values() if child.n != 0]
        best_move = max(possible_moves, key=lambda x: x[0])[1]
        self.game.make_move(best_move)