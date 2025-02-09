# # 1
# # # import numpy as np
# # # import random

# # # class Board:
# # #     def __init__(self):
# # #         self.board = np.full((2, 6), 4)  # 2 rows, 6 columns, 4 seeds per pit
# # #         self.stores = [0, 0]  # Captured seeds for Player 1 and Player 2

# # #     def reset(self):
# # #         self.board = np.full((2, 6), 4)
# # #         self.stores = [0, 0]

# # #     def capture_seeds(self, player, pit_row, pit_col):
# # #         seeds = self.board[pit_row, pit_col]
# # #         self.stores[player] += seeds
# # #         self.board[pit_row, pit_col] = 0

# # #     def is_empty(self):
# # #         return self.board.sum() == 0

# # #     def has_valid_moves(self, player):
# # #         row = 0 if player == 0 else 1
# # #         return np.any(self.board[row, :] > 0)


# # # class RuleEngine:
# # #     def __init__(self):
# # #         pass

# # #     def is_valid_move(self, player, row, col, board):
# # #         if player == 0 and row != 0:
# # #             return False
# # #         if player == 1 and row != 1:
# # #             return False
# # #         return board[row, col] > 0

# # #     def evaluate_capture(self, player, board, row, col):
# # #         return board[row, col] == 4


# # # class GameState:
# # #     def __init__(self, board):
# # #         self.board = board
# # #         self.log = []  # Keep track of actions
# # #         self.scores = board.stores

# # #     def update_state(self, player, action, capture):
# # #         self.log.append((player, action, capture))
# # #         self.scores = self.board.stores


# # # class Player:
# # #     def __init__(self, player_id):
# # #         self.player_id = player_id

# # #     def select_move(self, board):
# # #         row = 0 if self.player_id == 0 else 1
# # #         valid_pits = [col for col in range(6) if board[row, col] > 0]
# # #         if valid_pits:
# # #             return row, random.choice(valid_pits)
# # #         return None  # No valid moves


# # # class GameController:
# # #     def __init__(self):
# # #         self.board = Board()
# # #         self.rule_engine = RuleEngine()
# # #         self.state = GameState(self.board)
# # #         self.players = [Player(0), Player(1)]
# # #         self.current_player = 0

# # #     def reset(self):
# # #         self.board.reset()
# # #         self.state = GameState(self.board)
# # #         self.current_player = 0

# # #     def step(self):
# # #         player = self.players[self.current_player]
        
# # #         # Check if the current player has valid moves
# # #         if not self.board.has_valid_moves(self.current_player):
# # #             print(f"Player {self.current_player} has no valid moves")
# # #             self.current_player = 1 - self.current_player
# # #             return

# # #         move = player.select_move(self.board.board)
# # #         if not move:
# # #             print(f"Player {self.current_player} has no valid moves")
# # #             self.current_player = 1 - self.current_player
# # #             return

# # #         row, col = move
# # #         seeds = self.board.board[row, col]
# # #         self.board.board[row, col] = 0

# # #         # Sowing seeds counterclockwise
# # #         current_row, current_col = row, col
# # #         while seeds > 0:
# # #             current_col = (current_col + 1) % 6
# # #             if current_col == 0:
# # #                 current_row = 1 - current_row
# # #             self.board.board[current_row, current_col] += 1
# # #             seeds -= 1

# # #         # Evaluate captures
# # #         capture = False
# # #         if self.rule_engine.evaluate_capture(self.current_player, self.board.board, current_row, current_col):
# # #             self.board.capture_seeds(self.current_player, current_row, current_col)
# # #             capture = True

# # #         # Update game state
# # #         self.state.update_state(self.current_player, (row, col), capture)

# # #         # Switch player
# # #         self.current_player = 1 - self.current_player

# # #     def play(self):
# # #         while not self.board.is_empty():
# # #             self.step()
# # #         print("Game Over")
# # #         print(f"Scores: {self.board.stores}")
# # # # Run the game
# # # if __name__ == "__main__":
# # #     game = GameController()
# # #     game.reset()
# # #     game.play()


# # 2
# # # import numpy as np
# # # import random

# # # class Board:
# # #     def __init__(self):
# # #         self.board = np.full((2, 6), 4)  # 2 rows, 6 columns, 4 seeds per pit
# # #         self.stores = [0, 0]  # Captured seeds for Player 1 and Player 2
# # #         self.territories = [[0, 1, 2, 3, 4, 5], [0, 1, 2, 3, 4, 5]]

# # #     def reset(self):
# # #         self.board = np.full((2, 6), 4)
# # #         self.stores = [0, 0]
# # #         self.territories = [[0, 1, 2, 3, 4, 5], [0, 1, 2, 3, 4, 5]]

# # #     def capture_seeds(self, player, row, col):
# # #         seeds = self.board[row, col]
# # #         self.stores[player] += seeds
# # #         self.board[row, col] = 0

# # #     def is_empty(self):
# # #         return self.board.sum() == 0

# # #     def has_valid_moves(self, player):
# # #         row = 0 if player == 0 else 1
# # #         for col in self.territories[player]:
# # #             if self.board[row, col] > 0:
# # #                 return True
# # #         return False

# # #     def total_seeds(self):
# # #         return self.board.sum()

# # # class RuleEngine:
# # #     def __init__(self):
# # #         pass

# # #     def is_valid_move(self, player, row, col, board, territories):
# # #         if player == 0 and row != 0:
# # #             return False
# # #         if player == 1 and row != 1:
# # #             return False
# # #         if col not in territories[player]:
# # #             return False
# # #         return board[row, col] > 0

# # #     def evaluate_capture(self, player, board, row, col, territories):
# # #         if col in territories[player] and board[row, col] == 4:
# # #             return True
# # #         return False

# # # class Player:
# # #     def __init__(self, player_id):
# # #         self.player_id = player_id

# # #     def select_move(self, board, territories):
# # #         row = 0 if self.player_id == 0 else 1
# # #         valid_pits = [col for col in territories[self.player_id] if board[row, col] > 0]
# # #         if valid_pits:
# # #             return row, random.choice(valid_pits)
# # #         return None  # No valid moves

# # # class GameController:
# # #     def __init__(self):
# # #         self.board = Board()
# # #         self.rule_engine = RuleEngine()
# # #         self.players = [Player(0), Player(1)]
# # #         self.current_player = 0
# # #         self.round_wins = [0, 0]  # Tracks rounds won by each player

# # #     def reset_round(self):
# # #         self.board.reset()

# # #     def capture_territory(self, winner):
# # #         loser = 1 - winner
# # #         if self.board.territories[loser]:
# # #             captured_pit = self.board.territories[loser].pop()
# # #             self.board.territories[winner].append(captured_pit)

# # #     def step(self):
# # #         player = self.players[self.current_player]

# # #         # Check if the current player has valid moves
# # #         if not self.board.has_valid_moves(self.current_player):
# # #             print(f"Player {self.current_player} has no valid moves")
# # #             self.current_player = 1 - self.current_player
# # #             return

# # #         move = player.select_move(self.board.board, self.board.territories)
# # #         if not move:
# # #             print(f"Player {self.current_player} has no valid moves")
# # #             self.current_player = 1 - self.current_player
# # #             return

# # #         row, col = move
# # #         seeds = self.board.board[row, col]
# # #         self.board.board[row, col] = 0

# # #         # Sowing seeds counterclockwise
# # #         current_row, current_col = row, col
# # #         while seeds > 0:
# # #             current_col = (current_col + 1) % 6
# # #             if current_col == 0:
# # #                 current_row = 1 - current_row
# # #             self.board.board[current_row, current_col] += 1
# # #             seeds -= 1

# # #         # Evaluate captures
# # #         capture = False
# # #         if self.rule_engine.evaluate_capture(self.current_player, self.board.board, current_row, current_col, self.board.territories):
# # #             self.board.capture_seeds(self.current_player, current_row, current_col)
# # #             capture = True

# # #         # Switch player
# # #         self.current_player = 1 - self.current_player

# # #     def play_round(self):
# # #         while not self.board.is_empty():
# # #             self.step()

# # #         print("Round Over")
# # #         print(f"Scores: {self.board.stores}")

# # #         # Determine round winner
# # #         if self.board.stores[0] > self.board.stores[1]:
# # #             winner = 0
# # #         else:
# # #             winner = 1

# # #         self.round_wins[winner] += 1
# # #         self.capture_territory(winner)

# # #     def play(self):
# # #         while abs(self.round_wins[0] - self.round_wins[1]) < 6:
# # #             self.reset_round()
# # #             self.play_round()

# # #         overall_winner = 0 if self.round_wins[0] > self.round_wins[1] else 1
# # #         print(f"Game Over! Player {overall_winner} wins!")
# # #         print(f"Round Wins: {self.round_wins}")


# # # # Run the game
# # # if __name__ == "__main__":
# # #     game = GameController()
# # #     # game.reset()
# # #     game.play()

# # 3

# # # import numpy as np
# # # import random

# # # class Board:
# # #     def __init__(self):
# # #         self.board = np.full((2, 6), 4)  # 2 rows, 6 columns, 4 seeds per pit
# # #         self.stores = [0, 0]  # Captured seeds for Player 1 and Player 2
# # #         self.territories = [[0, 1, 2, 3, 4, 5], [0, 1, 2, 3, 4, 5]]

# # #     def reset(self):
# # #         self.board = np.full((2, 6), 4)
# # #         self.stores = [0, 0]

# # #     def capture_seeds(self, player, row, col):
# # #         seeds = self.board[row, col]
# # #         self.stores[player] += seeds
# # #         self.board[row, col] = 0

# # #     def is_empty(self):
# # #         return self.board.sum() == 0

# # #     def has_valid_moves(self, player):
# # #         row = 0 if player == 0 else 1
# # #         for col in self.territories[player]:
# # #             if self.board[row, col] > 0:
# # #                 return True
# # #         return False


# # # class RuleEngine:
# # #     def __init__(self):
# # #         pass

# # #     def is_valid_move(self, player, row, col, board, territories):
# # #         if player == 0 and row != 0:
# # #             return False
# # #         if player == 1 and row != 1:
# # #             return False
# # #         if col not in territories[player]:
# # #             return False
# # #         return board[row, col] > 0

# # #     def evaluate_capture(self, player, board, row, col, territories):
# # #         if col in territories[player] and board[row, col] == 4:
# # #             return True
# # #         return False


# # # class Player:
# # #     def __init__(self, player_id):
# # #         self.player_id = player_id

# # #     def select_move(self, board, territories):
# # #         row = 0 if self.player_id == 0 else 1
# # #         valid_pits = [col for col in territories[self.player_id] if board[row, col] > 0]
# # #         if valid_pits:
# # #             return row, random.choice(valid_pits)
# # #         return None  # No valid moves


# # # class GameState:
# # #     def __init__(self):
# # #         self.round = 0
# # #         self.scores = [0, 0]  # Stores the total captured seeds for each player

# # #     def update_state(self, player, score):
# # #         self.scores[player] += score


# # # class GameController:
# # #     def __init__(self):
# # #         self.board = Board()
# # #         self.rule_engine = RuleEngine()
# # #         self.players = [Player(0), Player(1)]
# # #         self.current_player = 0
# # #         self.state = GameState()

# # #     def reset_round(self):
# # #         self.board.reset()

# # #     def capture_territory(self, winner):
# # #         loser = 1 - winner
# # #         if self.board.territories[loser]:
# # #             captured_pit = self.board.territories[loser].pop()
# # #             self.board.territories[winner].append(captured_pit)

# # #     def step(self):
# # #         player = self.players[self.current_player]

# # #         # Check if the current player has valid moves
# # #         if not self.board.has_valid_moves(self.current_player):
# # #             print(f"Player {self.current_player} has no valid moves")
# # #             self.current_player = 1 - self.current_player
# # #             return

# # #         move = player.select_move(self.board.board, self.board.territories)
# # #         if not move:
# # #             print(f"Player {self.current_player} has no valid moves")
# # #             self.current_player = 1 - self.current_player
# # #             return

# # #         row, col = move
# # #         seeds = self.board.board[row, col]
# # #         self.board.board[row, col] = 0

# # #         # Sowing seeds counterclockwise
# # #         current_row, current_col = row, col
# # #         while seeds > 0:
# # #             current_col = (current_col + 1) % 6
# # #             if current_col == 0:
# # #                 current_row = 1 - current_row
# # #             self.board.board[current_row, current_col] += 1
# # #             seeds -= 1

# # #         # Evaluate captures
# # #         capture = False
# # #         if self.rule_engine.evaluate_capture(self.current_player, self.board.board, current_row, current_col, self.board.territories):
# # #             self.board.capture_seeds(self.current_player, current_row, current_col)
# # #             capture = True

# # #         # Update game state
# # #         if capture:
# # #             self.state.update_state(self.current_player, self.board.stores[self.current_player])

# # #         # Switch player
# # #         self.current_player = 1 - self.current_player

# # #     def play_round(self):
# # #         while not self.board.is_empty():
# # #             self.step()

# # #         print("Round Over")
# # #         print(f"Scores: {self.board.stores}")

# # #         # Determine round winner
# # #         winner = 0 if self.board.stores[0] > self.board.stores[1] else 1
# # #         self.capture_territory(winner)

# # #     def play(self):
# # #         while len(self.board.territories[0]) > 0 and len(self.board.territories[1]) > 0:
# # #             self.reset_round()
# # #             self.play_round()

# # #         overall_winner = 0 if len(self.board.territories[1]) == 0 else 1
# # #         print(f"Game Over! Player {overall_winner} wins!")
# # #         print(f"Final State: {self.state.scores}")


# # import numpy as np
# # import random

# # class Board:
# #     def __init__(self):
# #         self.board = np.full((2, 6), 4)
# #         self.stores = [0, 0]
# #         self.territories = [[0, 1, 2, 3, 4, 5], [0, 1, 2, 3, 4, 5]]
# #         self.captured_territories = [0, 0]

# #     def reset(self):
# #         self.board = np.full((2, 6), 4)
# #         self.stores = [0, 0]

# #     def capture_seeds(self, player, row, col):
# #         seeds = self.board[row, col]
# #         self.stores[player] += seeds
# #         self.board[row, col] = 0

# #     def is_empty(self):
# #         return self.board.sum() == 0

# #     def has_valid_moves(self, player):
# #         row = 0 if player == 0 else 1
# #         for col in self.territories[player]:
# #             if self.board[row, col] > 0:
# #                 return True
# #         return False

# #     def format_board(self):
# #         return f"[[{' '.join(map(str, self.board[0]))}]\n [{' '.join(map(str, self.board[1]))}]]"


# # class Player:
# #     def __init__(self, player_id):
# #         self.player_id = player_id
# #         self.score = 0
# #         self.captured_territories = 0

# #     def select_move(self, board, valid_moves):
# #         # For now, implementing random selection
# #         # Could be extended for AI or human input
# #         return random.choice(valid_moves)

# #     def get_row(self):
# #         return 0 if self.player_id == 0 else 1

# #     def get_player_number(self):
# #         return self.player_id + 1


# # class RuleEngine:
# #     def __init__(self):
# #         self.winning_territories = 3

# #     def is_valid_move(self, player, action, board):
# #         row = player.get_row()
# #         return (action in board.territories[player.player_id] and 
# #                 board.board[row, action] > 0)

# #     def execute_move(self, player, action, board):
# #         row = player.get_row()
# #         seeds = board.board[row, action]
# #         board.board[row, action] = 0

# #         current_row, current_col = row, action
# #         while seeds > 0:
# #             current_col = (current_col + 1) % 6
# #             if current_col == 0:
# #                 current_row = 1 - current_row
# #             board.board[current_row, current_col] += 1
# #             seeds -= 1

# #         return current_row, current_col

# #     def check_capture(self, player, opponent, final_row, final_col, board):
# #         if (board.board[final_row, final_col] == 4 and 
# #             final_col in board.territories[opponent.player_id]):
# #             board.territories[opponent.player_id].remove(final_col)
# #             board.territories[player.player_id].append(final_col)
# #             board.captured_territories[player.player_id] += 1
# #             player.captured_territories += 1

# #     def check_winner(self, players):
# #         for player in players:
# #             if player.captured_territories >= self.winning_territories:
# #                 return player
# #         return None


# # class GameState:
# #     def __init__(self):
# #         self.round = 1
# #         self.total_states = 0
# #         self.current_player_idx = 0
# #         self.game_over = False

# #     def increment_state(self):
# #         self.total_states += 1

# #     def switch_player(self):
# #         self.current_player_idx = 1 - self.current_player_idx

# #     def start_new_round(self):
# #         self.round += 1

# #     def print_game_state(self, board, current_player):
# #         print(f"\nSTART ROUND {self.round}\n")
# #         print("New Board:")
# #         print(board.format_board())
        
# #         print(f"Player {current_player.get_player_number()} starts this round")
# #         print(f"Current player: {current_player.get_player_number()}")
        
# #         options = board.territories[current_player.player_id]
# #         print(f"Player {current_player.get_player_number()} action options {options}")

# #     def print_move_result(self, board, current_player):
# #         print("\nCALCULATING REWARD ...")
        
# #         print("\nGAME STATE SAVING ...")
# #         print(board.format_board())
# #         print("GAME STATE SAVED ...")
# #         self.total_states += 1
# #         print(f"Total states saved ({self.total_states})")
        
# #         print("\nCurrent stores state:")
# #         print(f"[{board.stores[0]} {board.stores[1]}]")
# #         print("Current territory count:")
# #         print(f"[{len(board.territories[0])} {len(board.territories[1])}]")

# #         print("Switch Players ...")
# #         self.switch_player()
# #         print(f"Current player: {(self.current_player_idx + 1)}")
        
# #         options = board.territories[self.current_player_idx]
# #         print(f"Player {self.current_player_idx + 1} action options {options}")


# # class GameController:
# #     def __init__(self):
# #         self.board = Board()
# #         self.players = [Player(0), Player(1)]
# #         self.rule_engine = RuleEngine()
# #         self.state = GameState()

# #     def play_turn(self):
# #         current_player = self.players[self.state.current_player_idx]
# #         opponent = self.players[1 - self.state.current_player_idx]
        
# #         action = current_player.select_move(self.board, self.board.territories[current_player.player_id])
# #         print(f"\nPlayer {current_player.get_player_number()} chooses action: {action}")

# #         final_row, final_col = self.rule_engine.execute_move(current_player, action, self.board)
# #         self.rule_engine.check_capture(current_player, opponent, final_row, final_col, self.board)
# #         self.state.print_move_result(self.board, current_player)

# #         winner = self.rule_engine.check_winner(self.players)
# #         if winner:
# #             self.state.game_over = True
# #             print(f"\nGame Over! Player {winner.get_player_number()} wins!")
# #             print(f"Final territory captures: {[p.captured_territories for p in self.players]}")

# #     def play(self):
# #         while not self.state.game_over:
# #             self.state.print_game_state(self.board, self.players[self.state.current_player_idx])
# #             self.play_turn()
            
# #             if self.board.is_empty():
# #                 self.state.start_new_round()
# #                 self.board.reset()


# # if __name__ == "__main__":
# #     game = GameController()
# #     game.play()

# # import numpy as np
# # import random

# # class Board:
# #     def __init__(self):
# #         self.board = np.full((2, 6), 4)
# #         self.stores = [0, 0]
# #         self.territories = [[0, 1, 2, 3, 4, 5], [0, 1, 2, 3, 4, 5]]
# #         self.captured_territories = [0, 0]

# #     def reset(self):
# #         self.board = np.full((2, 6), 4)
# #         self.stores = [0, 0]

# #     def capture_seeds(self, player, row, col):
# #         seeds = self.board[row, col]
# #         self.stores[player] += seeds
# #         self.board[row, col] = 0

# #     def is_empty(self):
# #         return self.board.sum() == 0

# #     def has_valid_moves(self, player):
# #         row = 0 if player == 0 else 1
# #         for col in self.territories[player]:
# #             if self.board[row, col] > 0:
# #                 return True
# #         return False

# #     def format_board(self):
# #         return f"[[{' '.join(map(str, self.board[0]))}]\n [{' '.join(map(str, self.board[1]))}]]"


# # class Player:
# #     def __init__(self, player_id):
# #         self.player_id = player_id
# #         self.score = 0
# #         self.captured_territories = 0

# #     def select_move(self, board, valid_moves):
# #         return random.choice(valid_moves)

# #     def get_row(self):
# #         return 0 if self.player_id == 0 else 1

# #     def get_player_number(self):
# #         return self.player_id + 1


# # class RuleEngine:
# #     def __init__(self):
# #         self.winning_territories = 3

# #     def is_valid_move(self, player, action, board):
# #         row = player.get_row()
# #         return (action in board.territories[player.player_id] and 
# #                 board.board[row, action] > 0)

# #     def execute_move(self, player, action, board):
# #         row = player.get_row()
# #         seeds = board.board[row, action]
# #         board.board[row, action] = 0

# #         current_row, current_col = row, action
# #         while seeds > 0:
# #             current_col = (current_col + 1) % 6
# #             if current_col == 0:
# #                 current_row = 1 - current_row
# #             board.board[current_row, current_col] += 1
# #             seeds -= 1

# #         return current_row, current_col

# #     def check_capture(self, player, opponent, final_row, final_col, board):
# #         if (board.board[final_row, final_col] == 4 and 
# #             final_col in board.territories[opponent.player_id]):
# #             board.territories[opponent.player_id].remove(final_col)
# #             board.territories[player.player_id].append(final_col)
# #             board.captured_territories[player.player_id] += 1
# #             player.captured_territories += 1

# #     def check_winner(self, players):
# #         for player in players:
# #             if player.captured_territories >= self.winning_territories:
# #                 return player
# #         return None


# # class GameState:
# #     def __init__(self):
# #         self.round = 1
# #         self.total_states = 0
# #         self.current_player_idx = 0
# #         self.game_over = False

# #     def increment_state(self):
# #         self.total_states += 1

# #     def switch_player(self):
# #         self.current_player_idx = 1 - self.current_player_idx

# #     def start_new_round(self):
# #         self.round += 1

# #     def print_game_state(self, board, current_player):
# #         print(f"\nSTART ROUND {self.round}\n")
# #         print("New Board:")
# #         print(board.format_board())
        
# #         print(f"Player {current_player.get_player_number()} starts this round")
# #         print(f"Current player: {current_player.get_player_number()}")
        
# #         options = board.territories[current_player.player_id]
# #         print(f"Player {current_player.get_player_number()} action options {options}")

# #     def print_move_result(self, board, current_player):
# #         print("\nCALCULATING REWARD ...")
        
# #         print("\nGAME STATE SAVING ...")
# #         print(board.format_board())
# #         print("GAME STATE SAVED ...")
# #         self.total_states += 1
# #         print(f"Total states saved ({self.total_states})")
        
# #         print("\nCurrent stores state:")
# #         print(f"[{board.stores[0]} {board.stores[1]}]")
# #         print("Current territory count:")
# #         print(f"[{len(board.territories[0])} {len(board.territories[1])}]")

# #         print("Switch Players ...")
# #         self.switch_player()
# #         print(f"Current player: {(self.current_player_idx + 1)}")
        
# #         options = board.territories[self.current_player_idx]
# #         print(f"Player {self.current_player_idx + 1} action options {options}")


# # class GameController:
# #     def __init__(self):
# #         self.board = Board()
# #         self.players = [Player(0), Player(1)]
# #         self.rule_engine = RuleEngine()
# #         self.state = GameState()

# #     def play_turn(self):
# #         try:
# #             current_player = self.players[self.state.current_player_idx]
# #             opponent = self.players[1 - self.state.current_player_idx]
            
# #             action = current_player.select_move(self.board, self.board.territories[current_player.player_id])
# #             print(f"\nPlayer {current_player.get_player_number()} chooses action: {action}")

# #             final_row, final_col = self.rule_engine.execute_move(current_player, action, self.board)
# #             self.rule_engine.check_capture(current_player, opponent, final_row, final_col, self.board)
# #             self.state.print_move_result(self.board, current_player)

# #             winner = self.rule_engine.check_winner(self.players)
# #             if winner:
# #                 self.state.game_over = True
# #                 print(f"\nGame Over! Player {winner.get_player_number()} wins!")
# #                 print(f"Final territory captures: {[p.captured_territories for p in self.players]}")

# #         except Exception as e:
# #             print(f"Error during play turn: {e}")
# #             self.state.game_over = True

# #     def play(self):
# #         while not self.state.game_over:
# #             self.state.print_game_state(self.board, self.players[self.state.current_player_idx])
# #             self.play_turn()
            
# #             if self.board.is_empty():
# #                 self.state.start_new_round()
# #                 self.board.reset()
# #                 print("\nRound reset, stores updated:")
# #                 print(f"Stores: {self.board.stores}")


# # if __name__ == "__main__":
# #     game = GameController()
# #     game.play()
# #     input("\nPress Enter to exit the game.")

# # import numpy as np
# # import random

# # class Board:
# #     def __init__(self):
# #         self.board = np.full((2, 6), 4)
# #         self.stores = [0, 0]
# #         self.territories = [[0, 1, 2, 3, 4, 5], [0, 1, 2, 3, 4, 5]]

# #     def reset(self):
# #         self.board = np.full((2, 6), 4)
# #         self.stores = [0, 0]

# #     def is_empty(self):
# #         return self.board.sum() == 0

# #     def has_valid_moves(self, player):
# #         row = 0 if player == 0 else 1
# #         for col in self.territories[player]:
# #             if self.board[row, col] > 0:
# #                 return True
# #         return False

# #     def format_board(self):
# #         return f"[[{' '.join(map(str, self.board[0]))}]\n [{' '.join(map(str, self.board[1]))}]]"


# # class Player:
# #     def __init__(self, player_id):
# #         self.player_id = player_id
# #         self.captured_territories = 0

# #     def select_move(self, board, valid_moves):
# #         return random.choice(valid_moves)

# #     def get_row(self):
# #         return 0 if self.player_id == 0 else 1

# #     def get_player_number(self):
# #         return self.player_id + 1


# # class RuleEngine:
# #     def __init__(self):
# #         self.winning_territories = 7

# #     def is_valid_move(self, player, action, board):
# #         row = player.get_row()
# #         return (action in board.territories[player.player_id] and 
# #                 board.board[row, action] > 0)

# #     def execute_move(self, player, action, board):
# #         row = player.get_row()
# #         seeds = board.board[row, action]
# #         board.board[row, action] = 0

# #         current_row, current_col = row, action
# #         while seeds > 0:
# #             current_col = (current_col + 1) % 6
# #             if current_col == 0:
# #                 current_row = 1 - current_row
# #             board.board[current_row, current_col] += 1
# #             seeds -= 1

# #         return current_row, current_col

# #     def check_capture(self, player, opponent, final_row, final_col, board):
# #         if (board.board[final_row, final_col] == 4 and 
# #             final_col in board.territories[opponent.player_id]):
# #             board.territories[opponent.player_id].remove(final_col)
# #             board.territories[player.player_id].append(final_col)

# #             player.captured_territories += 1
# #             opponent.captured_territories -= 1

# #     def check_winner(self, players):
# #         for player in players:
# #             if player.captured_territories >= self.winning_territories:
# #                 return player
# #         return None


# # class GameState:
# #     def __init__(self):
# #         self.round = 1
# #         self.total_states = 0
# #         self.current_player_idx = 0
# #         self.game_over = False

# #     def increment_state(self):
# #         self.total_states += 1

# #     def switch_player(self):
# #         self.current_player_idx = 1 - self.current_player_idx

# #     def start_new_round(self):
# #         self.round += 1

# #     def print_game_state(self, board, current_player):
# #         print(f"\nSTART ROUND {self.round}\n")
# #         print("New Board:")
# #         print(board.format_board())
# #         print(f"Player {current_player.get_player_number()} starts this round")
# #         print(f"Current player: {current_player.get_player_number()}")
# #         print(f"Player {current_player.get_player_number()} action options {board.territories[current_player.player_id]}")

# #     def print_move_result(self, board, current_player):
# #         print("\nCALCULATING REWARD ...")
# #         print("\nGAME STATE SAVING ...")
# #         print(board.format_board())
# #         print("GAME STATE SAVED ...")
# #         self.increment_state()
# #         print(f"Total states saved ({self.total_states})")
# #         print("\nCurrent stores state:")
# #         print(f"[{board.stores[0]} {board.stores[1]}]")
# #         print("Current territory count:")
# #         print(f"[{len(board.territories[0])} {len(board.territories[1])}]")
# #         print("Switch Players ...")
# #         self.switch_player()
# #         print(f"Current player: {(self.current_player_idx + 1)}")
# #         print(f"Player {self.current_player_idx + 1} action options {board.territories[self.current_player_idx]}")


# # class GameController:
# #     def __init__(self):
# #         self.board = Board()
# #         self.players = [Player(0), Player(1)]
# #         self.rule_engine = RuleEngine()
# #         self.state = GameState()

# #     def play_turn(self):
# #         current_player = self.players[self.state.current_player_idx]
# #         opponent = self.players[1 - self.state.current_player_idx]
        
# #         action = current_player.select_move(self.board, self.board.territories[current_player.player_id])
# #         print(f"\nPlayer {current_player.get_player_number()} chooses action: {action}")

# #         final_row, final_col = self.rule_engine.execute_move(current_player, action, self.board)
# #         self.rule_engine.check_capture(current_player, opponent, final_row, final_col, self.board)
# #         self.state.print_move_result(self.board, current_player)

# #         winner = self.rule_engine.check_winner(self.players)
# #         if winner:
# #             self.state.game_over = True
# #             print(f"\nGame Over! Player {winner.get_player_number()} wins!")
# #             print(f"Final territory captures: {[p.captured_territories for p in self.players]}")

# #     def play(self):
# #         while not self.state.game_over:
# #             self.state.print_game_state(self.board, self.players[self.state.current_player_idx])
# #             self.play_turn()
            
# #             if self.board.is_empty():
# #                 self.state.start_new_round()
# #                 self.board.reset()

# #         input("\nPress Enter to exit...")


# # if __name__ == "__main__":
# #     game = GameController()
# #     game.play()

# import numpy as np
# import random


# class Board:
#     def __init__(self):
#         self.board = np.full((2, 6), 4)
#         self.stores = [0, 0]
#         self.territories = [[0, 1, 2, 3, 4, 5], [0, 1, 2, 3, 4, 5]]

#     def reset(self):
#         self.board = np.full((2, 6), 4)
#         self.stores = [0, 0]

#     def is_empty(self):
#         return self.board.sum() == 0

#     def has_valid_moves(self, player):
#         row = 0 if player == 0 else 1
#         for col in self.territories[player]:
#             if self.board[row, col] > 0:
#                 return True
#         return False

#     def format_board(self):
#         return f"[[{' '.join(map(str, self.board[0]))}]\n [{' '.join(map(str, self.board[1]))}]]"


# class Player:
#     def __init__(self, player_id):
#         self.player_id = player_id
#         self.captured_territories = 0

#     def select_move(self, board, valid_moves):
#         return random.choice(valid_moves)

#     def get_row(self):
#         return 0 if self.player_id == 0 else 1

#     def get_player_number(self):
#         return self.player_id + 1


# class RuleEngine:
#     def __init__(self):
#         self.winning_territories = 6

#     def is_valid_move(self, player, action, board):
#         row = player.get_row()
#         return (action in board.territories[player.player_id] and 
#                 board.board[row, action] > 0)

#     def execute_move(self, player, action, board):
#         row = player.get_row()
#         seeds = board.board[row, action]
#         board.board[row, action] = 0

#         current_row, current_col = row, action
#         while seeds > 0:
#             current_col = (current_col + 1) % 6
#             if current_col == 0:
#                 current_row = 1 - current_row
#             board.board[current_row, current_col] += 1
#             seeds -= 1

#         return current_row, current_col

#     def check_capture(self, player, opponent, final_row, final_col, board):
#         if (board.board[final_row, final_col] == 4 and 
#             final_col in board.territories[opponent.player_id]):
#             board.territories[opponent.player_id].remove(final_col)
#             board.territories[player.player_id].append(final_col)

#             player.captured_territories += 1
#             opponent.captured_territories -= 1

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

#     def increment_state(self):
#         self.total_states += 1

#     def switch_player(self):
#         self.current_player_idx = 1 - self.current_player_idx

#     def start_new_round(self):
#         self.round += 1

#     def print_game_state(self, board, current_player):
#         print(f"\nSTART ROUND {self.round}\n")
#         print("New Board:")
#         print(board.format_board())
#         print(f"Player {current_player.get_player_number()} starts this round")
#         print(f"Player {current_player.get_player_number()} action options {board.territories[current_player.player_id]}")

#     def print_move_result(self, board, current_player):
#         print("\nCALCULATING REWARD ...")
#         print("\nGAME STATE SAVING ...")
#         print(board.format_board())
#         print("GAME STATE SAVED ...")
#         self.increment_state()
#         print(f"Total states saved ({self.total_states})")
#         print("\nCurrent stores state:")
#         print(f"[{board.stores[0]} {board.stores[1]}]")
#         print("Current territory count:")
#         print(f"[{len(board.territories[0])} {len(board.territories[1])}]")
#         print("Switch Players ...")
#         self.switch_player()
#         print(f"Current player: {(self.current_player_idx + 1)}")
#         print(f"Player {self.current_player_idx + 1} action options {board.territories[self.current_player_idx]}")


# class GameController:
#     def __init__(self):
#         self.board = Board()
#         self.players = [Player(0), Player(1)]
#         self.rule_engine = RuleEngine()
#         self.state = GameState()

#     def play_turn(self):
#         current_player = self.players[self.state.current_player_idx]
#         opponent = self.players[1 - self.state.current_player_idx]
        
#         action = current_player.select_move(self.board, self.board.territories[current_player.player_id])
#         print(f"\nPlayer {current_player.get_player_number()} chooses action: {action}")

#         final_row, final_col = self.rule_engine.execute_move(current_player, action, self.board)
#         self.rule_engine.check_capture(current_player, opponent, final_row, final_col, self.board)
#         self.state.print_move_result(self.board, current_player)

#         winner = self.rule_engine.check_winner(self.players)
#         if winner:
#             self.state.game_over = True
#             print(f"\nGame Over! Player {winner.get_player_number()} wins!")
#             print(f"Final territory captures: {[p.captured_territories for p in self.players]}")

#     def play(self):
#         while not self.state.game_over:
#             self.state.print_game_state(self.board, self.players[self.state.current_player_idx])
#             self.play_turn()
            
#             if self.board.is_empty():
#                 self.state.start_new_round()
#                 self.board.reset()

#         input("\nPress Enter to exit...")


# if __name__ == "__main__":
#     game = GameController()
#     game.play()
