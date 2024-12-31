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
    
    def get_flattened_state(self):
        """
        Returns the current board state as a flattened array.
        """
        flat_board = np.array(self.state.board.board).flatten()
        store = np.array(self.state.board.store)
        return np.concatenate((flat_board, store))


    def step(self, action):
        """
        Executes the action for the current player and updates the game state.

        Args:
            action (int): Action chosen by the current player.

        Returns:
            tuple: (flattened_state, reward, done, valid_actions)
        """
        current_player = self.state.current_player
        board = self.state.board

        # Get valid actions for the current player
        valid_actions = [
            i for i in range(6) if board.is_valid_move(current_player, current_player, i)
        ]

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

        # Flatten the board state and append the stores
        flattened_state = np.concatenate(
            [np.array(board.board).flatten(), np.array(board.store)]
        )

        # Debugging: Print the flattened state
        print(f"Flattened State: {flattened_state}")

        return flattened_state, reward, done, valid_actions

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
