```markdown
# Oware RL Agents

This project implements reinforcement learning agents (PPO and DDQN) to play the Oware Nam-Nam game.

## Project Structure

- `game/`: Game logic and board management.
- `agents/`: RL agent implementations.
- `utils/`: Utility functions for replay buffer and metrics.
- `main.py`: Entry point for training and evaluation.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/oware_rl.git
   cd oware_rl
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Train Agents

To train the PPO agent:
```bash
python main.py --train ppo
```

To train the DDQN agent:
```bash
python main.py --train ddqn
```

### Evaluate Agents

To evaluate performance:
```bash
python main.py --evaluate ppo --opponent random
```

## Metrics

1. **Win Rate**: Percentage of games won by the agent.
2. **Average Reward**: Mean reward per game.
3. **Training Stability**: Loss and reward trends during training.

---

## **Step 3: Steps to Run Scripts and Evaluation**

### **3.1 Running the Scripts**

1. **Train PPO Agent**:
   ```bash
   python main.py --train ppo
   ```

2. **Train DDQN Agent**:
   ```bash
   python main.py --train ddqn
   ```

3. **Evaluate PPO Against DDQN**:
   ```bash
   python main.py --evaluate ppo --opponent ddqn
   ```

---

### **3.2 Metrics for Comparison**

1. **Win Rate**:
   - Percentage of games won by PPO and DDQN against a random agent and each other.

2. **Reward Trends**:
   - Plot cumulative rewards during training to assess learning efficiency.

3. **Training Stability**:
   - Measure the loss and variance in rewards during training.

---

Let me know if you’d like me to start implementing this structure or focus on specific parts!
