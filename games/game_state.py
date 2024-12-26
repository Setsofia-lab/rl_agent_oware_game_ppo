from board import Board

class GameState:
    def __init__(self):
        self.board = Board()
        self.current_player = 0
        self.rounds_played = 0
    
    def switch_player(self):
        self.current_player = 1 - self.current_player
    
    def get_state(self):
        return self.board.board, self.board.store
