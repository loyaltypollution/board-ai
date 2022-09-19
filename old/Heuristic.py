from copy import deepcopy

from BasicAlgorithms import RandomAlgorithm

class Heuristic:
    def __init__(self, gameclass):
        self.gameclass = gameclass
    
    def evaluate(self, gamestate):
        pass
    
    def random_playout(self, gamestate, n=1):
        results  = [0 for i in range(self.gameclass.playercount)]
        players = [RandomAlgorithm() for i in range(self.gameclass.playercount)]
        for i in range(n):
            simulated_game = self.gameclass(*players)
            simulated_game.gamestate = gamestate
            score = simulated_game.get_score(simulated_game.game_start(True))
            results = [result + score[index] for index, result in enumerate(results)]
        
        results = [result / n for result in results]
        return results