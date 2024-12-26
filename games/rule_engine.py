class RuleEngine:
    @staticmethod
    def calculate_reward(player, captured_seeds, game_won=False):
        """
        Calculates the reward for the player based on seeds captured and game outcome.
        
        Args:
            player (int): The ID of the player (0 or 1).
            captured_seeds (int): Number of seeds captured in the turn.
            game_won (bool): Whether the player has won the game.
        
        Returns:
            int: Calculated reward.
        """
        reward = 10 * captured_seeds
        if game_won:
            reward += 100
        return reward

    @staticmethod
    def is_game_over(board):
        """
        Checks if the game is over. The game ends when:
        1. A player's side of the board is empty, or
        2. Both players cannot make a valid move.
        
        Args:
            board (Board): The game board object.
        
        Returns:
            bool: True if the game is over, False otherwise.
        """
        # Check if either player's side is empty
        player_1_empty = all(pit == 0 for pit in board.board[0])
        player_2_empty = all(pit == 0 for pit in board.board[1])

        # Check if neither player has valid moves
        no_valid_moves = (
            all(pit == 0 for pit in board.board[0]) and
            all(pit == 0 for pit in board.board[1])
        )

        return player_1_empty or player_2_empty or no_valid_moves

    @staticmethod
    def determine_game_winner(board):
        """
        Determines the winner based on the number of seeds in the players' stores.

        Args:
            board (Board): The game board object.

        Returns:
            int: 0 if player 1 wins, 1 if player 2 wins, -1 for a tie.
        """
        if board.store[0] > board.store[1]:
            return 0  # Player 1 wins
        elif board.store[1] > board.store[0]:
            return 1  # Player 2 wins
        else:
            return -1  # Tie

