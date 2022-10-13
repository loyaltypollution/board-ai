;import random

from Heuristic import Heuristic
from BasicAlgorithms import PlayerTemplate

class GeneticAlgorithm(PlayerTemplate):

    def __init__(self, population_size, generations, heuristic):
        self.population_size = population_size
        self.generations = generations
        self.heuristic = heuristic
        
        self.architecture = {'Selection':['tournament_selection', {}], 'Crossover':['uniform_crossover', {'instance':self}], 'Mutation':['jump_mutation', {'instance':self}]}

    def register_game(self, game):
        self.game = game
        self.load_player(self.filename, ['heuristic', 'architecture'])
    
    def get_architecture(self):
        for component, descriptor in self.architecture.items():
            print(component, 'uses', descriptor[0], 'with arguments', *descriptor[1].items())
    
    class Selection:     
        def tournament_selection(population, p, k):
            tournament = random.choices(population, k=k)
            tournament = sorted(tournament, key=lambda x:x.get_fitness())
            selected = []
            for i in range(k):
                probability = p*pow((1-p),i)
                if random.random() < probability:
                    selected.append(tournament[i])
            return selected
        def proportional_selection(population):
            print('proportional')
            return population
        def niching_selection(population):
            print('niching')
            return population

    class Crossover:        
        def point_crossover(population):
            return population
        def uniform_crossover(population, instance):
            population = [parent[1] for parent in population]
            duration = len(population)
            for i in range(duration):
                parents = random.choices(population,k=2)
                child = sum([parents[random.randint(0,1)] & (1 << i) for i in range(max(instance.genomes).bit_length())])
                if child in instance.genomes:
                    population.append(child)
            return population

    class Mutation:        
        def jump_mutation(population, instance):
            children = []
            for parent in population:
                child = parent
                while random.random() < 0.2:
                    pos = random.randint(0, max(instance.genomes).bit_length()-1)
                    child = parent ^ 1 << pos
                if child != parent and child in instance.genomes:
                    children += [child]
            return population + children
        def creep_mutation(population):
            print('proportional')
            return population
    
    class Cell:
        def seed():
            Cell.seed_from_gamestates()
        
        def encode():
            return bitstring
        
        def seed_from_gamestates():
       
            def get_gametree(gameclass, gamestate, depth = 999):
                '''returns the gametree as a list.
                each element is a list containing all moves to arrive at an unique leaf'''
                all_moves = gameclass.get_legal_moves(gamestate)
                if len(all_moves) == 0 or depth == 0:
                    return [[]]
                gametree = []
                for move in all_moves:
                    next_iteration = get_gametree(gameclass.project_move(gamestate, move), depth - 1)
                    movesets = [[move]+i for i in next_iteration]
                    gametree += movesets
                return gametree
            
            dna_range = get_gametree()
            
    
    
    def get_gamestate_from_history(self, history):
        gamestate = self.game.gamestate
        for move in history:
            gamestate = self.game.project_move(gamestate, move)
        return gamestate
    
    def move(self):
        seed_population = Cell.seed_from_gamestates(self.game.gamestate, 4)
        
        seed_population = self.get_leaves(depth = 4)
        self.genomes = list(range(0, len(seed_population)))
        population = random.choices(self.genomes, k = 10)
        print(population, len(self.genomes))                  
        def get_fitness(index, history):
            gamestate = self.get_gamestate_from_history(history)
            score = self.heuristic.evaluate(gamestate)
            score = score[self.game.gamestate['turn']]
            return (score, index)
        
        for i in range(self.depth):
            population = [get_fitness(index, seed_population[index]) for index in population]
            for component, descriptor in self.architecture.items():
                population = getattr(getattr(self, component), descriptor[0])(population = population, **descriptor[1])
            print(population)
        wait = int(input('hello'))
        return seed_population[wait]