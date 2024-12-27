## **Overview of the Project**

This project builds an RL agent to play the Oware game. It includes two reinforcement learning methods: **Double Deep Q-Networks (DDQN)** and **Proximal Policy Optimization (PPO)**. The project also visualizes the board and evaluates the agents' performance.

---

### **Step-by-Step Implementation**

#### **1. Directory and File Structure**

```plaintext
RL_agent_oware/
├── main.py                 # Entry point for training and evaluation
├── games/
│   ├── __init__.py         # Marks `games` as a Python module
│   ├── board.py            # Board mechanics and operations
│   ├── rule_engine.py      # Game rules and reward calculations
│   ├── game_state.py       # Tracks the game state
│   └── game_controller.py  # Manages gameplay and agents
├── agents/
│   ├── __init__.py         # Marks `agents` as a Python module
│   ├── ddqn_agent.py       # Double Deep Q-Network implementation
│   ├── ppo_agent.py        # Proximal Policy Optimization agent
│   └── random_agent.py     # Random agent for baseline comparison
├── utils/
│   ├── __init__.py         # Marks `utils` as a Python module
│   ├── metrics.py          # Evaluation metrics (e.g., win rate)
│   └── memory_buffer.py    # Replay buffer for experience storage
└── README.md               # Documentation
```

---

### **2. Detailed Explanation of Each File and Key Functions**

#### **`board.py`**
Handles the mechanics of the Oware board.

- **`__init__`**: Initializes the board with two rows of pits, each containing 4 seeds, and two stores (one for each player).
- **`reset`**: Resets the board to its initial state.
- **`sow`**: Implements the sowing logic. Seeds from a selected pit are distributed counterclockwise across the board.
- **`is_valid_move`**: Checks if a move is valid (e.g., the selected pit has seeds and belongs to the current player).
- **`capture_seeds`**: Captures seeds based on the rules (e.g., if the last pit contains 2 or 3 seeds in the opponent's row).

#### **`rule_engine.py`**
Implements game rules and reward logic.

- **`calculate_reward`**: Calculates rewards based on seeds captured and whether the player won.
- **`is_game_over`**: Checks if the game has ended:
  - Either player's pits are empty, or neither player can make a valid move.
- **`determine_game_winner`**: Determines the winner based on seeds in each player's store.

#### **`game_state.py`**
Tracks the current state of the game.

- **`GameState`**:
  - Maintains the board and player information.
  - Provides `switch_player` to alternate between players.
  - Provides `get_state` to return the current board state.

#### **`game_controller.py`**
Manages the flow of the game and integrates agents.

- **`step`**:
  - Executes a move by the current player.
  - Updates the board, calculates rewards, and switches turns.
  - Returns the updated board state, reward, and game status.
- **`visualize_board`**:
  - Displays the current board state using `matplotlib` for visualization.

#### **`ddqn_agent.py`**
Implements Double Deep Q-Network (DDQN).

- **`act`**: Selects an action using an epsilon-greedy strategy.
- **`train`**:
  - Samples experiences from the replay buffer.
  - Updates the Q-network using the DDQN logic to reduce overestimation bias.
  - Returns the average loss for debugging and performance tracking.

#### **`ppo_agent.py`**
Implements Proximal Policy Optimization (PPO).

- **`act`**: Chooses an action based on the policy network.
- **`train`**:
  - Updates the policy network using the clipped PPO objective.
  - Updates the value network to estimate the state value.

#### **`random_agent.py`**
Implements a simple baseline agent.

- **`act`**: Selects a valid move randomly.

#### **`metrics.py`**
Provides evaluation metrics.

- **`calculate_win_rate`**: Simulates games to calculate the agent’s win rate.
- **`calculate_average_reward`**: Computes the average reward over multiple games.

#### **`main.py`**
Orchestrates training, evaluation, and visualization.

- **`train_agent`**:
  - Trains the specified RL agent.
  - Includes optional visualization of the board state.
- **`evaluate_agents`**:
  - Evaluates agents against each other using metrics like win rate and average reward.

---

### **3. Logic Behind the Oware Game**

Oware is a two-player strategy game played on a board with two rows of six pits and two stores (one for each player). 

#### **Rules Implemented:**
1. **Sowing**:
   - Seeds from a chosen pit are distributed counterclockwise, one seed per pit.
   - If the last seed lands in an opponent's pit with 2 or 3 seeds, they are captured.

2. **Winning**:
   - The game ends when either player cannot make a valid move, or all pits are empty.
   - The player with the most seeds in their store wins.

3. **Rewards**:
   - Capturing seeds yields rewards.
   - A bonus reward is given for winning.

---

### **4. Rationale for Choosing RL Agents**

#### **Double Deep Q-Network (DDQN)**:
- **Strengths**:
  - Handles large state spaces by approximating Q-values with a neural network.
  - Reduces overestimation bias in action-value estimation compared to DQN.
- **Reason**: Oware’s state space is large, and DDQN is effective for discrete action spaces with a clear reward structure.

#### **Proximal Policy Optimization (PPO)**:
- **Strengths**:
  - Directly optimizes policies, allowing continuous improvement.
  - Stabilizes learning using a clipped surrogate objective.
- **Reason**: PPO can effectively handle stochastic environments and encourages exploration through entropy regularization.

---

### **5. Key Issues Encountered and Fixes**

1. **ModuleNotFoundError**:
   - Resolved by adding `__init__.py` files and using relative imports.
2. **Invalid Moves**:
   - Ensured agents only select valid moves by providing a list of valid actions.
3. **Loss Accumulation Error**:
   - Fixed the `train` method in `DDQNAgent` to return average loss per batch.
4. **Visualization Integration**:
   - Used `matplotlib` to display the board state during training.

---

### **6. Summary of RL Agent Logic**

1. **DDQN**:
   - Learns action-value mappings using Q-learning.
   - Reduces overestimation of Q-values using a separate target network.
   - Suitable for discrete action spaces like Oware.

2. **PPO**:
   - Optimizes a policy directly using gradient descent.
   - Stabilizes training with a clipped objective to prevent drastic policy updates.
   - Encourages exploration, making it well-suited for strategic games.
