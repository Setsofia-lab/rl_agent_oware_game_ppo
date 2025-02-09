from games.game_controller import GameController
from agents.random_agent import RandomAgent
from agents.dqn import DQNPlayer

def main():
    # Initialize the game with a DQN player and a random player
    game = GameController()
    game.players = [DQNPlayer(0), RandomAgent(1)]  # Player 0: DQN, Player 1: Random
    game.play()

if __name__ == "__main__":
    main()
