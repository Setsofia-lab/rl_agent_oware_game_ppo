class Board:
    def __init__(self):
        self.board = [[4] * 6, [4] * 6]  # Two rows with 6 pits each
        self.store = [0, 0]  # Player stores for captured seeds
    
    def reset(self):
        self.__init__()
    
    def sow(self, row, pit):
        # Handles sowing seeds logic
        pass

    def is_valid_move(self, player, row, pit):
        # Returns True if the move is valid
        pass

    def capture_seeds(self, player, row, pit):
        # Handles capturing seeds
        pass
