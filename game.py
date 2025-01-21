import numpy as np
import random

class Board:
    def __init__(self):
        self.board = np.full((2, 6), 4)
        self.stores = [0, 0]
        self.territories = [[0, 1, 2, 3, 4, 5], [0, 1, 2, 3, 4, 5]]
        self.captured_territories = [0, 0]

    def reset(self):
        self.board = np.full((2, 6), 4)
        self.stores = [0, 0]

    def capture_seeds(self, player, row, col):
        seeds = self.board[row, col]
        self.stores[player] += seeds
        self.board[row, col] = 0

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


class Player:
    def __init__(self, player_id):
        self.player_id = player_id
        self.score = 0
        self.captured_territories = 0

    def select_move(self, board, valid_moves):
        # For now, implementing random selection
        # Could be extended for AI or human input
        return random.choice(valid_moves)

    def get_row(self):
        return 0 if self.player_id == 0 else 1

    def get_player_number(self):
        return self.player_id + 1


class RuleEngine:
    def __init__(self):
        self.winning_territories = 3

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
            board.captured_territories[player.player_id] += 1
            player.captured_territories += 1

    def check_winner(self, players):
        for player in players:
            if player.captured_territories >= self.winning_territories:
                return player
        return None


class GameState:
    def __init__(self):
        self.round = 1
        self.total_states = 0
        self.current_player_idx = 0
        self.game_over = False

    def increment_state(self):
        self.total_states += 1

    def switch_player(self):
        self.current_player_idx = 1 - self.current_player_idx

    def start_new_round(self):
        self.round += 1

    def print_game_state(self, board, current_player):
        print(f"\nSTART ROUND {self.round}\n")
        print("New Board:")
        print(board.format_board())
        
        print(f"Player {current_player.get_player_number()} starts this round")
        print(f"Current player: {current_player.get_player_number()}")
        
        options = board.territories[current_player.player_id]
        print(f"Player {current_player.get_player_number()} action options {options}")

    def print_move_result(self, board, current_player):
        print("\nCALCULATING REWARD ...")
        
        print("\nGAME STATE SAVING ...")
        print(board.format_board())
        print("GAME STATE SAVED ...")
        self.total_states += 1
        print(f"Total states saved ({self.total_states})")
        
        print("\nCurrent stores state:")
        print(f"[{board.stores[0]} {board.stores[1]}]")
        print("Current territory count:")
        print(f"[{len(board.territories[0])} {len(board.territories[1])}]")

        print("Switch Players ...")
        self.switch_player()
        print(f"Current player: {(self.current_player_idx + 1)}")
        
        options = board.territories[self.current_player_idx]
        print(f"Player {self.current_player_idx + 1} action options {options}")


class GameController:
    def __init__(self):
        self.board = Board()
        self.players = [Player(0), Player(1)]
        self.rule_engine = RuleEngine()
        self.state = GameState()

    def play_turn(self):
        current_player = self.players[self.state.current_player_idx]
        opponent = self.players[1 - self.state.current_player_idx]
        
        action = current_player.select_move(self.board, self.board.territories[current_player.player_id])
        print(f"\nPlayer {current_player.get_player_number()} chooses action: {action}")

        final_row, final_col = self.rule_engine.execute_move(current_player, action, self.board)
        self.rule_engine.check_capture(current_player, opponent, final_row, final_col, self.board)
        self.state.print_move_result(self.board, current_player)

        winner = self.rule_engine.check_winner(self.players)
        if winner:
            self.state.game_over = True
            print(f"\nGame Over! Player {winner.get_player_number()} wins!")
            print(f"Final territory captures: {[p.captured_territories for p in self.players]}")

    def play(self):
        while not self.state.game_over:
            self.state.print_game_state(self.board, self.players[self.state.current_player_idx])
            self.play_turn()
            
            if self.board.is_empty():
                self.state.start_new_round()
                self.board.reset()


if __name__ == "__main__":
    game = GameController()
    game.play()