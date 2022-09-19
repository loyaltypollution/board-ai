class GameTemplate:
    playercount = 2
    def __init__(self, *players):
        '''initializes class with gamestate, players and history '''
        self.gamestate = self.get_starting_gamestate()
        self.players = players
        self.history = []
            
        self.register_players()
        assert(len(self.players)==self.playercount)

    def get_starting_gamestate(self):
        '''dictionary containing all data needed to describe the game
            format is data_name : data
        '''
        return {}
    
    def register_players(self):
        for player in self.players:
            player.register_game(self)
            
    def get_legal_moves(self, gamestate = None):
        '''given a gamestate, returns the possible moves that can be taken.
        if gamestate not specified, assume current gamestate'''
        return []
        
    def project_move(self, gamestate, move):
        '''given a gamestate and a move, returns the resultant gamestate.
        if gamestate not specified, assume current gamestate'''
        return {}
    
    def make_move(self, move):
        '''registers a move in its gamestate. update history with said move'''
        self.gamestate = self.project_move(self.gamestate, move)
        self.history.append(move)
    
    def user_instructions(self):
        '''function meant to be overwritten.
        return a list of strings describing the inputs that users have to key in'''
        move = self.get_legal_moves(self.get_starting_gamestate())[0]
        if isinstance(move, int):
            return ['input']
        if isinstance(move, tuple):
            return ['input '+str(i+1) for i in range(len(move))]
        raise Exception('unspecified user instructions')
        
    def get_boardstate(self, gamestate = None):
        '''given a boardstate, pretty-prints all information requried.
        if gamestate not specified, assume current gamestate'''
        if not gamestate:
            gamestate = self.gamestate
        pass
    
    def result(self, gamestate = None):
        '''given a boardstate, returns the outcome of the game.
        if gamestate not specified, assume current gamestate'''
        if not gamestate:
            gamestate = self.gamestate
        pass
    
    def get_winner(self, result):
        '''given an outcome of the game, reports the winner.'''
        if result == 'player 0 won':
            return 0
        if result == 'player 1 won':
            return 1
        if result == 'draw':
            return 0.5
        return -1
    
    def get_score(self, result):
        '''given an outcome of the game, reports score differential.'''
        if result == 'player 0 won':
            return [1,0]
        if result == 'player 1 won':
            return [0,1]
        if result == 'draw':
            return [0.5, 0.5]
        return [0,0]
        
    def game_start(self, hide = False):
        '''driver function to play the game'''
        while self.result() == 'pending':
            turn = self.gamestate['turn']
            self.players[turn].move()
        if not hide:
            self.get_boardstate()
        return self.result()