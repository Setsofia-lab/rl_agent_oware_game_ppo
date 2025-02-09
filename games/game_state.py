
class GameState:
    def __init__(self):
        self.round = 1
        self.total_states = 0
        self.current_player_idx = 0
        self.game_over = False
        self.max_rounds = 100  # Add a maximum number of rounds

    def increment_state(self):
        self.total_states += 1

    def switch_player(self):
        self.current_player_idx = 1 - self.current_player_idx

    def start_new_round(self):
        self.round += 1
        if self.round > self.max_rounds:  # End the game if max rounds reached
            self.game_over = True

    def print_game_state(self, board, current_player):
        print(f"\nSTART ROUND {self.round}\n")
        print("New Board:")
        print(board.format_board())
        print(f"Player {current_player.get_player_number()} starts this round")
        print(f"Player {current_player.get_player_number()} action options {board.territories[current_player.player_id]}")

    def print_move_result(self, board, current_player):
        print("\nCALCULATING REWARD ...")
        print("\nGAME STATE SAVING ...")
        print(board.format_board())
        print("GAME STATE SAVED ...")
        self.increment_state()
        print(f"Total states saved ({self.total_states})")
        print("\nCurrent stores state:")
        print(f"[{board.stores[0]} {board.stores[1]}]")
        print("Current territory count:")
        print(f"[{len(board.territories[0])} {len(board.territories[1])}]")
        print("Switch Players ...")
        self.switch_player()
        print(f"Current player: {(self.current_player_idx + 1)}")
        print(f"Player {self.current_player_idx + 1} action options {board.territories[self.current_player_idx]}")
