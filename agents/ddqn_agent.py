import random
import numpy as np
from collections import deque
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import Adam

class DDQNAgent:
    def __init__(self, state_size, action_size):
        self.state_size = state_size
        self.action_size = action_size
        self.memory = deque(maxlen=2000)
        self.gamma = 0.99  # Discount factor
        self.epsilon = 1.0  # Exploration rate
        self.epsilon_decay = 0.995
        self.epsilon_min = 0.01
        self.learning_rate = 0.001
        self.model = self._build_model()
        self.target_model = self._build_model()
        self.update_target_model()

    def _build_model(self):
        model = Sequential()
        model.add(Dense(128, input_dim=self.state_size, activation='relu'))
        model.add(Dense(128, activation='relu'))
        model.add(Dense(self.action_size, activation='linear'))
        model.compile(loss='mse', optimizer=Adam(learning_rate=self.learning_rate))
        return model

    def update_target_model(self):
        self.target_model.set_weights(self.model.get_weights())

    def remember(self, state, action, reward, next_state, done):
        self.memory.append((state, action, reward, next_state, done))

    # def act(self, state):
    #     if np.random.rand() <= self.epsilon:
    #         return random.randrange(self.action_size)
    #     q_values = self.model.predict(np.array([state]), verbose=0)
    #     return np.argmax(q_values[0])
    
    def act(self, state, valid_actions=None):
        """
        Chooses an action based on the current policy.

        Args:
            state (array-like): Current board state.
            valid_actions (list): List of valid action indices.

        Returns:
            int: Chosen action index.
        """
        if np.random.rand() <= self.epsilon:
            # Random exploration: Choose only from valid actions
            if valid_actions:
                return np.random.choice(valid_actions)
            return random.randrange(self.action_size)
        
        q_values = self.model.predict(np.array([state]), verbose=0)
        if valid_actions:
            # Mask invalid actions
            q_values = [q if i in valid_actions else -np.inf for i, q in enumerate(q_values[0])]
            return np.argmax(q_values)
        
        return np.argmax(q_values[0])



    def train(self, batch_size):
        if len(self.memory) < batch_size:
            return 0  # Return 0 loss if there aren't enough samples

        minibatch = random.sample(self.memory, batch_size)
        total_loss = 0

        for state, action, reward, next_state, done in minibatch:
            target = self.model.predict(np.array([state]), verbose=0)[0]
            if done:
                target[action] = reward
            else:
                next_action = np.argmax(self.model.predict(np.array([next_state]), verbose=0)[0])
                target[action] = reward + self.gamma * self.target_model.predict(np.array([next_state]), verbose=0)[0][next_action]

            history = self.model.fit(np.array([state]), np.array([target]), epochs=1, verbose=0)
            total_loss += history.history['loss'][0]  # Accumulate loss from this batch

        if self.epsilon > self.epsilon_min:
            self.epsilon *= self.epsilon_decay

        return total_loss / batch_size  # Return average loss



