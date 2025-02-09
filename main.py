

# import numpy as np
# import random

# class Board:
#     def __init__(self):
#         self.board = np.full((2, 6), 4)
#         self.stores = [0, 0]
#         self.territories = [[0, 1, 2, 3, 4, 5], [0, 1, 2, 3, 4, 5]]
#         self.captured_territories = [0, 0]

#     def reset(self):
#         self.board = np.full((2, 6), 4)
#         self.stores = [0, 0]

#     def capture_seeds(self, player, row, col):
#         seeds = self.board[row, col]
#         self.stores[player] += seeds
#         self.board[row, col] = 0

#     def is_empty(self):
#         return self.board.sum() == 0

#     def has_valid_moves(self, player):
#         row = 0 if player == 0 else 1
#         return any(self.board[row, col] > 0 for col in self.territories[player])

#     def format_board(self):
#         return f"[[{' '.join(map(str, self.board[0]))}]\n [{' '.join(map(str, self.board[1]))}]]"


# class Player:
#     def __init__(self, player_id):
#         self.player_id = player_id
#         self.score = 0
#         self.captured_territories = 0

#     def select_move(self, board, valid_moves):
#         # Filter out moves with no seeds
#         row = self.get_row()
#         available_moves = [move for move in valid_moves 
#                          if board.board[row, move] > 0]
#         if not available_moves:
#             return None
#         return random.choice(available_moves)

#     def get_row(self):
#         return 0 if self.player_id == 0 else 1

#     def get_player_number(self):
#         return self.player_id + 1


# class RuleEngine:
#     def __init__(self):
#         self.winning_territories = 3

#     def is_valid_move(self, player, action, board):
#         if action is None:
#             return False
#         row = player.get_row()
#         return (action in board.territories[player.player_id] and 
#                 board.board[row, action] > 0)

#     def execute_move(self, player, action, board):
#         try:
#             row = player.get_row()
#             seeds = board.board[row, action]
#             board.board[row, action] = 0

#             current_row, current_col = row, action
#             while seeds > 0:
#                 current_col = (current_col + 1) % 6
#                 if current_col == 0:
#                     current_row = 1 - current_row
#                 board.board[current_row, current_col] += 1
#                 seeds -= 1

#             return current_row, current_col
#         except Exception as e:
#             print(f"Error executing move: {e}")
#             return row, action

#     def check_capture(self, player, opponent, final_row, final_col, board):
#         try:
#             if (board.board[final_row, final_col] == 4 and 
#                 final_col in board.territories[opponent.player_id]):
#                 board.territories[opponent.player_id].remove(final_col)
#                 if final_col not in board.territories[player.player_id]:
#                     board.territories[player.player_id].append(final_col)
#                     board.captured_territories[player.player_id] += 1
#                     player.captured_territories += 1
#         except Exception as e:
#             print(f"Error in capture: {e}")

#     def check_winner(self, players):
#         for player in players:
#             if player.captured_territories >= self.winning_territories:
#                 return player
#         return None


# class GameState:
#     def __init__(self):
#         self.round = 1
#         self.total_states = 0
#         self.current_player_idx = 0
#         self.game_over = False
#         self.max_rounds = 100  # Safety limit

#     def increment_state(self):
#         self.total_states += 1

#     def switch_player(self):
#         self.current_player_idx = 1 - self.current_player_idx

#     def start_new_round(self):
#         self.round += 1
#         if self.round > self.max_rounds:
#             self.game_over = True
#             print(f"Game ended due to reaching maximum rounds ({self.max_rounds})")

#     def print_game_state(self, board, current_player):
#         print(f"\nSTART ROUND {self.round}\n")
#         print("New Board:")
#         print(board.format_board())
        
#         print(f"Player {current_player.get_player_number()} starts this round")
#         print(f"Current player: {current_player.get_player_number()}")
        
#         options = [opt for opt in board.territories[current_player.player_id]
#                   if board.board[current_player.get_row(), opt] > 0]
#         print(f"Player {current_player.get_player_number()} action options {options}")

#     def print_move_result(self, board, current_player):
#         print("\nCALCULATING REWARD ...")
        
#         print("\nGAME STATE SAVING ...")
#         print(board.format_board())
#         print("GAME STATE SAVED ...")
#         self.total_states += 1
#         print(f"Total states saved ({self.total_states})")
        
#         print("\nCurrent stores state:")
#         print(f"[{board.stores[0]} {board.stores[1]}]")
#         print("Current territory count:")
#         print(f"[{len(board.territories[0])} {len(board.territories[1])}]")

#         print("Switch Players ...")
#         self.switch_player()
#         print(f"Current player: {(self.current_player_idx + 1)}")
        
#         next_player = self.current_player_idx
#         valid_options = [opt for opt in board.territories[next_player]
#                         if board.board[1 if next_player else 0, opt] > 0]
#         print(f"Player {next_player + 1} action options {valid_options}")


# class GameController:
#     def __init__(self):
#         self.board = Board()
#         self.players = [Player(0), Player(1)]
#         self.rule_engine = RuleEngine()
#         self.state = GameState()

#     def play_turn(self):
#         try:
#             current_player = self.players[self.state.current_player_idx]
#             opponent = self.players[1 - self.state.current_player_idx]
            
#             # Check if current player has valid moves
#             if not self.board.has_valid_moves(current_player.player_id):
#                 print(f"Player {current_player.get_player_number()} has no valid moves")
#                 self.state.switch_player()
#                 return

#             action = current_player.select_move(self.board, self.board.territories[current_player.player_id])
#             if action is None:
#                 print(f"Player {current_player.get_player_number()} has no valid moves")
#                 self.state.switch_player()
#                 return

#             print(f"\nPlayer {current_player.get_player_number()} chooses action: {action}")

#             final_row, final_col = self.rule_engine.execute_move(current_player, action, self.board)
#             self.rule_engine.check_capture(current_player, opponent, final_row, final_col, self.board)
#             self.state.print_move_result(self.board, current_player)

#             winner = self.rule_engine.check_winner(self.players)
#             if winner:
#                 self.state.game_over = True
#                 print(f"\nGame Over! Player {winner.get_player_number()} wins!")
#                 print(f"Final territory captures: {[p.captured_territories for p in self.players]}")

#         except Exception as e:
#             print(f"Error in play_turn: {e}")
#             self.state.game_over = True

#     def play(self):
#         try:
#             while not self.state.game_over:
#                 self.state.print_game_state(self.board, self.players[self.state.current_player_idx])
#                 self.play_turn()
                
#                 if self.board.is_empty():
#                     self.state.start_new_round()
#                     self.board.reset()

#         except Exception as e:
#             print(f"Error in play: {e}")


# if __name__ == "__main__":
#     game = GameController()
#     game.play()

import numpy as np
import random


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


class Player:
    def __init__(self, player_id):
        self.player_id = player_id
        self.captured_territories = 0

    def select_move(self, board, valid_moves):
        return random.choice(valid_moves)

    def get_row(self):
        return 0 if self.player_id == 0 else 1

    def get_player_number(self):
        return self.player_id + 1


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
            return

        if self.board.is_empty():
            self.state.start_new_round()
            self.board.reset()

    def play(self):
        while not self.state.game_over:
            self.state.print_game_state(self.board, self.players[self.state.current_player_idx])
            self.play_turn()

        input("\nPress Enter to exit...")


if __name__ == "__main__":
    game = GameController()
    game.play()