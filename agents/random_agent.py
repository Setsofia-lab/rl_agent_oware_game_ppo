# import random

# class RandomAgent:
#     def __init__(self, player_id):
#         self.player_id = player_id

#     def select_move(self, board, valid_moves):
#         return random.choice(valid_moves)

import random

class RandomAgent:
    def __init__(self, player_id):
        self.player_id = player_id

    def select_move(self, board, valid_moves):
        return random.choice(valid_moves)

    def get_row(self):
        return 0 if self.player_id == 0 else 1

    def get_player_number(self):
        return self.player_id + 1