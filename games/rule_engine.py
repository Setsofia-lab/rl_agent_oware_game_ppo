class RuleEngine:
    @staticmethod
    def calculate_reward(player, captured_seeds, game_won=False):
        reward = 10 * captured_seeds
        if game_won:
            reward += 100
        return reward

    @staticmethod
    def is_game_over(board):
        # Determines if the game has ended
        pass
