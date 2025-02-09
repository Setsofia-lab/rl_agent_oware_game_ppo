# Oware Game with Reinforcement Learning

Welcome to the Oware RL project! This project creates AI agents that learn to play Oware, an ancient African board game, using two different reinforcement learning approaches.

## What is Oware?

Oware is a strategic two-player game played on a board with 12 pits (6 per player) and 2 stores. Players take turns picking up seeds from their pits and distributing them around the board. The goal is to capture more seeds than your opponent by carefully planning your moves.

## Project Overview

I've built two AI agents that can learn and play Oware:
1. A Double Deep Q-Network (DDQN) agent that learns by estimating the value of different moves
2. A Proximal Policy Optimization (PPO) agent that learns by directly improving its strategy

I also included a random-move agent as a baseline for comparison.

## Project Structure

The project is organized into three main parts:

### 1. Game Engine (`games/`)
- `board.py`: Handles the game board mechanics and seed movement
- `rule_engine.py`: Implements game rules and scoring
- `game_state.py`: Keeps track of the current game state
- `game_controller.py`: Manages gameplay and visualization

### 2. AI Agents (`agents/`)
- `ddqn_agent.py`: The Double Deep Q-Network agent
- `ppo_agent.py`: The Proximal Policy Optimization agent
- `random_agent.py`: A simple agent that makes random moves

### 3. Support Tools (`utils/`)
- `metrics.py`: Tools for measuring agent performance
- `memory_buffer.py`: Storage system for the agents' learning experiences

## How the AI Works

### DDQN Agent
This agent works like a chess player who learns which moves are good by estimating their value. It uses two neural networks to avoid being too optimistic about move values, which helps it learn more effectively.

### PPO Agent
This agent learns more like a human player, directly improving its strategy through trial and error. It makes gradual improvements to avoid forgetting what it has learned, and maintains a good balance between trying new strategies and sticking to what works.

## The Game Rules

The core rules we've implemented:
1. Players distribute seeds counter-clockwise from their chosen pit
2. If your last seed lands in an opponent's pit that now has 2 or 3 seeds, you capture them
3. The game ends when a player can't make a valid move
4. The player with the most captured seeds wins

## Getting Started

1. Clone this repository
2. Install the required packages
3. Run `main.py` to start training or evaluating the agents

## Project Highlights

- Both AI agents can learn and improve their gameplay over time
- Includes visualization tools to watch the agents play
- Provides metrics to track how well the agents are performing
- Implements the complete ruleset of Oware

## Common Issues

If you run into any problems:
1. Make sure you can make valid moves (the agents will help with this)
2. If you see unusual behavior during training, the visualization tools can help debug
3. The game metrics will help you track if the agents are actually improving

Need more details about a specific part of the project? Feel free to check the code comments or open an issue!
