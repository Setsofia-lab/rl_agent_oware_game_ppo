import random

class RandomAgent:
    def __init__(self, action_size):
        self.action_size = action_size

    def act(self, state):
        # Get all pits with seeds as valid actions
        valid_actions = [i for i in range(self.action_size) if state[i] > 0]
        if not valid_actions:
            return None  # No valid actions
        return random.choice(valid_actions)
