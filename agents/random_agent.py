import random

class RandomAgent:
    def __init__(self, player_id):
        self.player_id = player_id

    def select_move(self, board, valid_moves):
        return random.choice(valid_moves)