class Board:
    def __init__(self):
        self.board = [[4] * 6, [4] * 6]  # Two rows with 6 pits each
        self.store = [0, 0]  # Player stores for captured seeds
    
    def reset(self):
        self.__init__()
    
    def sow(self, row, pit):
        seeds = self.board[row][pit]
        self.board[row][pit] = 0
        current_row, current_pit = row, pit

        while seeds > 0:
            current_pit += 1
            if current_pit >= 6:  # Move to the next row
                current_pit = 0
                current_row = 1 - current_row

            if current_row == row and current_pit == pit:
                continue  # Skip the starting pit

            self.board[current_row][current_pit] += 1
            seeds -= 1

        return current_row, current_pit  # Last sowing position

    def is_valid_move(self, player, row, pit):
        return row == player and self.board[row][pit] > 0

    def capture_seeds(self, player, row, pit):
        captured_seeds = 0
        while self.board[row][pit] in [2, 3] and row != player:
            captured_seeds += self.board[row][pit]
            self.board[row][pit] = 0
            pit -= 1
            if pit < 0:
                row = 1 - row
                pit = 5

        self.store[player] += captured_seeds
        return captured_seeds

