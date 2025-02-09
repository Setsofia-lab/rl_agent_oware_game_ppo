class RuleEngine:
    def __init__(self):
        self.winning_territories = 6

    def is_valid_move(self, player, action, board):
        row = player.get_row()
        return (action in board.territories[player.player_id] and 
                board.board[row, action] > 0)

    def execute_move(self, player, action, board):
        row = player.get_row()
        seeds = board.board[row, action]
        board.board[row, action] = 0

        current_row, current_col = row, action
        while seeds > 0:
            current_col = (current_col + 1) % 6
            if current_col == 0:
                current_row = 1 - current_row
            board.board[current_row, current_col] += 1
            seeds -= 1

        return current_row, current_col

    def check_capture(self, player, opponent, final_row, final_col, board):
        if (board.board[final_row, final_col] == 4 and 
            final_col in board.territories[opponent.player_id]):
            board.territories[opponent.player_id].remove(final_col)
            board.territories[player.player_id].append(final_col)

            player.captured_territories += 1
            opponent.captured_territories -= 1

            # Capture the seeds
            captured_seeds = board.board[final_row, final_col]
            board.board[final_row, final_col] = 0
            board.stores[player.player_id] += captured_seeds

    def check_winner(self, players):
        for player in players:
            if player.captured_territories >= self.winning_territories:
                return player
        return None