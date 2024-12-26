from games.game_controller import GameController
from agents.random_agent import RandomAgent

def calculate_win_rate(agent, opponent, num_games):
    wins = 0
    for _ in range(num_games):
        game_controller = GameController(agent, opponent)
        winner = game_controller.play_game()
        if winner == agent:
            wins += 1
    return wins / num_games

def calculate_average_reward(agent, num_games):
    total_reward = 0
    for _ in range(num_games):
        game_controller = GameController(agent, RandomAgent())
        total_reward += game_controller.play_game()
    return total_reward / num_games

