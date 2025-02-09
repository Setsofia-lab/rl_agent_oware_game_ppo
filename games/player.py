class Player:
    def __init__(self, player_id):
        self.player_id = player_id
        self.captured_territories = 0

    def select_move(self, board, valid_moves):
        raise NotImplementedError("Subclasses must implement select_move method.")

    def get_row(self):
        return 0 if self.player_id == 0 else 1

    def get_player_number(self):
        return self.player_id + 1