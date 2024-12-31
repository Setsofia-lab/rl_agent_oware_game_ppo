import tensorflow as tf
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input, Dense
from tensorflow.keras.optimizers import Adam
import numpy as np

class PPOAgent:
    def __init__(self, state_size, action_size):
        self.state_size = state_size
        self.action_size = action_size
        self.gamma = 0.99
        self.epsilon = 0.2  # Clipping ratio
        self.learning_rate = 0.0003

        self.policy_model, self.value_model = self._build_models()

    def _build_models(self):
        state_input = Input(shape=(self.state_size,))
        common = Dense(128, activation='relu')(state_input)
        common = Dense(128, activation='relu')(common)

        action_output = Dense(self.action_size, activation='softmax')(common)
        value_output = Dense(1, activation='linear')(common)

        policy_model = Model(inputs=state_input, outputs=action_output)
        policy_model.compile(optimizer=Adam(learning_rate=self.learning_rate))

        value_model = Model(inputs=state_input, outputs=value_output)
        value_model.compile(optimizer=Adam(learning_rate=self.learning_rate))

        return policy_model, value_model

    def act(self, state, valid_actions=None):
        """
        Selects an action based on the policy network.

        Args:
            state (array-like): Flattened board state.
            valid_actions (list): A list of valid actions.

        Returns:
            int: Chosen action.
        """
        # Ensure state is a flat 1D numpy array
        state = np.array(state, dtype=np.float32).flatten()

        # Debugging: Print state shape and policy probabilities
        print(f"Processed State Shape: {state.shape}")

        policy = self.policy_model.predict(state.reshape(1, -1), verbose=0)[0]

        if valid_actions:
            # Mask invalid actions
            masked_policy = np.zeros_like(policy)
            masked_policy[valid_actions] = policy[valid_actions]
            masked_policy /= np.sum(masked_policy)  # Re-normalize probabilities
            return np.random.choice(self.action_size, p=masked_policy)

        # Use the unfiltered policy
        return np.random.choice(self.action_size, p=policy)

    def train(self, states, actions, rewards, next_states, dones):
        advantages = rewards + self.gamma * self.value_model.predict(next_states) * (1 - dones) - self.value_model.predict(states)

        actions_one_hot = tf.keras.utils.to_categorical(actions, self.action_size)
        with tf.GradientTape() as tape:
            policy = self.policy_model(states, training=True)
            old_policy = tf.stop_gradient(policy)
            ratios = tf.reduce_sum(policy * actions_one_hot, axis=1) / tf.reduce_sum(old_policy * actions_one_hot, axis=1)
            clipped_ratios = tf.clip_by_value(ratios, 1 - self.epsilon, 1 + self.epsilon)
            loss = -tf.reduce_mean(tf.minimum(ratios * advantages, clipped_ratios * advantages))

        grads = tape.gradient(loss, self.policy_model.trainable_variables)
        self.policy_model.optimizer.apply_gradients(zip(grads, self.policy_model.trainable_variables))

        self.value_model.fit(states, rewards, verbose=0)

