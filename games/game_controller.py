import matplotlib.pyplot as plt
import numpy as np
from .game_state import GameState
from .rule_engine import RuleEngine
# from rule_engine import RuleEngine

class GameController:
    def __init__(self, agent1, agent2):
        self.agent1 = agent1
        self.agent2 = agent2
        self.state = GameState()

    def reset(self):
        self.state = GameState()
        return self.state.get_state()

    # def step(self, action):
    #     current_player = self.state.current_player
    #     board, store = self.state.board, self.state.board.store

    #     if not board.is_valid_move(current_player, action // 6, action % 6):
    #         raise ValueError(f"Invalid move by player {current_player}: {action}")

    #     row, pit = divmod(action, 6)
    #     last_row, last_pit = board.sow(row, pit)
    #     captured = board.capture_seeds(current_player, last_row, last_pit)
    #     reward = RuleEngine.calculate_reward(current_player, captured)
    #     done = RuleEngine.is_game_over(board)

    #     self.visualize_board()

    #     if not done:
    #         self.state.switch_player()

    #     return board.board, reward, done

    def step(self, action):
        current_player = self.state.current_player
        board = self.state.board

        # Get valid actions for the current player
        valid_actions = [
            i for i in range(6) if board.is_valid_move(current_player, current_player, i)
        ]

        # Debugging: Print board state and valid actions
        print(f"Player {current_player}'s turn.")
        print(f"Current Board: {board.board}")
        print(f"Valid Actions: {valid_actions}")
        print(f"Chosen Action: {action}")

        # Ensure the action is valid
        if action not in valid_actions:
            raise ValueError(f"Invalid move by player {current_player}: {action}")

        # Perform the move
        row, pit = divmod(action, 6)
        last_row, last_pit = board.sow(row, pit)
        captured = board.capture_seeds(current_player, last_row, last_pit)
        reward = RuleEngine.calculate_reward(current_player, captured)
        done = RuleEngine.is_game_over(board)

        # Switch players if the game is not over
        if not done:
            self.state.switch_player()

        # Return the new state, reward, and game status
        return board.board, reward, done, valid_actions




    def visualize_board(self):
        """Displays the current state of the Oware board."""
        fig, ax = plt.subplots()
        board = np.array(self.state.board.board)
        store = self.state.board.store

        # Draw the board as a grid
        ax.matshow(np.zeros((2, 6)), cmap="Greys", alpha=0.1)
        for (i, j), val in np.ndenumerate(board):
            ax.text(j, i, f'{val}', va='center', ha='center', color='black', fontsize=12)

        # Draw the player stores
        ax.text(-1, 0.5, f'P1 Store: {store[0]}', va='center', ha='right', fontsize=10)
        ax.text(6, 1.5, f'P2 Store: {store[1]}', va='center', ha='left', fontsize=10)

        # Remove axes
        ax.axis('off')

        plt.pause(0.5)  # Pause to show the updated state
        plt.close(fig)
