import numpy as np

class Board:
    def __init__(self):
        self.board = np.full((2, 6), 4)
        self.stores = [0, 0]
        self.territories = [[0, 1, 2, 3, 4, 5], [0, 1, 2, 3, 4, 5]]

    def reset(self):
        self.board = np.full((2, 6), 4)
        self.stores = [0, 0]

    def is_empty(self):
        return self.board.sum() == 0

    def has_valid_moves(self, player):
        row = 0 if player == 0 else 1
        for col in self.territories[player]:
            if self.board[row, col] > 0:
                return True
        return False

    def format_board(self):
        return f"[[{' '.join(map(str, self.board[0]))}]\n [{' '.join(map(str, self.board[1]))}]]"