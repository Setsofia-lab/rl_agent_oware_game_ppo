import argparse
from games.board import Board
from games.game_controller import GameController
from agents.ddqn_agent import DDQNAgent
from agents.ppo_agent import PPOAgent
from agents.random_agent import RandomAgent
from utils.metrics import calculate_win_rate, calculate_average_reward


def train_agent(agent_type, state_size, action_size, num_episodes, batch_size, visualize=False):
    if agent_type == "ddqn":
        agent = DDQNAgent(state_size, action_size)
    elif agent_type == "ppo":
        agent = PPOAgent(state_size, action_size)
    else:
        raise ValueError("Unsupported agent type. Use 'ddqn' or 'ppo'.")

    opponent = RandomAgent(action_size)
    game_controller = GameController(agent, opponent)
    losses, entropies = [], []

    for episode in range(num_episodes):
        state = game_controller.reset()
        done = False
        episode_loss, episode_entropy = 0, 0

        while not done:
            _, _, _, valid_actions = game_controller.step(0)  # Get valid actions
            action = agent.act(state, valid_actions=valid_actions)
            next_state, reward, done, valid_actions = game_controller.step(action)

            if visualize:
                game_controller.visualize_board()

            if agent_type == "ddqn":
                agent.remember(state, action, reward, next_state, done)
                loss = agent.train(batch_size)
                episode_loss += loss if loss else 0  # Accumulate loss only if it's not None
            elif agent_type == "ppo":
                episode_entropy += agent.train(state, action, reward, next_state, done)

            state = next_state

        # Update target network for DDQN
        if agent_type == "ddqn" and episode % 10 == 0:
            agent.update_target_model()

        losses.append(episode_loss)
        entropies.append(episode_entropy)

        print(f"Episode {episode + 1}/{num_episodes} completed.")
        return agent, losses, entropies



def evaluate_agents(agent1, agent2, num_games):
    print(f"Evaluating {agent1.__class__.__name__} vs {agent2.__class__.__name__}...")

    agent1_win_rate = calculate_win_rate(agent1, agent2, num_games)
    agent2_win_rate = 1 - agent1_win_rate
    agent1_avg_reward = calculate_average_reward(agent1, num_games)
    agent2_avg_reward = calculate_average_reward(agent2, num_games)

    print(f"Results:\n")
    print(f"{agent1.__class__.__name__}:")
    print(f"- Win Rate: {agent1_win_rate * 100:.2f}%")
    print(f"- Average Reward: {agent1_avg_reward:.2f}")
    print(f"\n{agent2.__class__.__name__}:")
    print(f"- Win Rate: {agent2_win_rate * 100:.2f}%")
    print(f"- Average Reward: {agent2_avg_reward:.2f}")


def main():
    parser = argparse.ArgumentParser(description="Train and evaluate Oware RL agents.")
    parser.add_argument("--train", choices=["ddqn", "ppo"], help="Type of agent to train.")
    parser.add_argument("--evaluate", action="store_true", help="Enable evaluation mode.")
    parser.add_argument("--episodes", type=int, default=100, help="Number of training episodes.")
    parser.add_argument("--games", type=int, default=50, help="Number of evaluation games.")
    parser.add_argument("--batch_size", type=int, default=64, help="Batch size for training.")
    parser.add_argument("--visualize", action="store_true", help="Enable board visualization during training.")

    args = parser.parse_args()

    state_size = 12  # Board size: 12 pits
    action_size = 12  # Actions: selecting any of the 12 pits

    if args.train:
        print(f"Training {args.train.upper()} agent...")
        agent, losses, entropies = train_agent(args.train, state_size, action_size, args.episodes, args.batch_size, visualize=args.visualize)

        if args.train == "ddqn":
            print(f"Training Loss (DDQN): {sum(losses) / len(losses):.2f}")
        elif args.train == "ppo":
            print(f"Policy Entropy (PPO): {sum(entropies) / len(entropies):.2f}")

    if args.evaluate:
        print("Evaluating trained agents...")
        ddqn_agent = DDQNAgent(state_size, action_size)  # Load trained DDQN agent
        ppo_agent = PPOAgent(state_size, action_size)  # Load trained PPO agent
        random_agent = RandomAgent(action_size)

        # Evaluate DDQN vs Random
        evaluate_agents(ddqn_agent, random_agent, args.games)
        # Evaluate PPO vs Random
        evaluate_agents(ppo_agent, random_agent, args.games)
        # Evaluate PPO vs DDQN
        evaluate_agents(ppo_agent, ddqn_agent, args.games)


if __name__ == "__main__":
    main()
