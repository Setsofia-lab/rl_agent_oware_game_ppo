import numpy as np
import random
from collections import deque
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.regularizers import l2

class DQNPlayer:
    def __init__(self, player_id, state_size=12, action_size=6):
        self.player_id = player_id
        self.state_size = state_size
        self.action_size = action_size
        self.memory = deque(maxlen=2000)  # Experience replay buffer
        self.gamma = 0.99                 # Discount factor
        self.epsilon = 0.6                # Exploration rate
        self.epsilon_min = 0.01
        self.epsilon_decay = 0.995
        self.learning_rate = 0.0001
        self.model = self._build_model()  # Primary network
        self.target_model = self._build_model()  # Target network
        self.update_target_model()
        self.batch_size = 32
        self.train_frequency = 10         # Train every 10 steps
        self.target_update_frequency = 10  # Update target network every 10 epochs

    def _build_model(self):
        """Build the DQN with 6 hidden layers, ReLU, and L2 regularization."""
        model = Sequential()
        model.add(Dense(128, input_dim=self.state_size, activation='relu', 
                       kernel_initializer='random_normal', kernel_regularizer=l2(0.01)))
        model.add(Dense(128, activation='relu', 
                       kernel_initializer='random_normal', kernel_regularizer=l2(0.01)))
        model.add(Dense(128, activation='relu', 
                       kernel_initializer='random_normal', kernel_regularizer=l2(0.01)))
        model.add(Dense(128, activation='relu', 
                       kernel_initializer='random_normal', kernel_regularizer=l2(0.01)))
        model.add(Dense(128, activation='relu', 
                       kernel_initializer='random_normal', kernel_regularizer=l2(0.01)))
        model.add(Dense(128, activation='relu', 
                       kernel_initializer='random_normal', kernel_regularizer=l2(0.01)))
        model.add(Dense(self.action_size, activation='linear'))
        model.compile(loss='mse', optimizer=Adam(learning_rate=self.learning_rate))
        return model

    def update_target_model(self):
        """Sync target network weights with the primary network."""
        self.target_model.set_weights(self.model.get_weights())

    def remember(self, state, action, reward, next_state, done):
        """Store experience in replay buffer."""
        self.memory.append((state, action, reward, next_state, done))

    def act(self, state, valid_moves):
        """Select action using epsilon-greedy policy with valid moves masking."""
        if np.random.rand() <= self.epsilon:
            return random.choice(valid_moves)
        state = np.reshape(state, [1, self.state_size])
        act_values = self.model.predict(state, verbose=0)
        # Mask invalid actions
        masked_act_values = np.full_like(act_values[0], -np.inf)
        for move in valid_moves:
            masked_act_values[move] = act_values[0][move]
        return np.argmax(masked_act_values)

    def replay(self):
        """Train the model using experiences from the replay buffer."""
        if len(self.memory) < self.batch_size:
            return
        minibatch = random.sample(self.memory, self.batch_size)
        states = np.array([t[0] for t in minibatch])
        actions = np.array([t[1] for t in minibatch])
        rewards = np.array([t[2] for t in minibatch])
        next_states = np.array([t[3] for t in minibatch])
        dones = np.array([t[4] for t in minibatch])

        # Predict Q-values using target network
        target_q = self.target_model.predict(next_states, verbose=0)
        targets = rewards + self.gamma * np.amax(target_q, axis=1) * (1 - dones)
        target_f = self.model.predict(states, verbose=0)
        for i, action in enumerate(actions):
            target_f[i][action] = targets[i]
        # Train the model
        self.model.fit(states, target_f, epochs=1, verbose=0)
        # Decay exploration rate
        if self.epsilon > self.epsilon_min:
            self.epsilon *= self.epsilon_decay

    def select_move(self, board, valid_moves):
        """Select move based on current board state and valid moves."""
        state = board.board.flatten()
        return self.act(state, valid_moves)