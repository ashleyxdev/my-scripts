#pip install gymnasium[toy_text]
# Experiment 8: Taxi Problem using Reinforcement Learning (Gymnasium Version)
# ---------------------------------------------------------------------------

import gymnasium as gym
import numpy as np
import random
from IPython.display import clear_output

# Step 1: Initialize Environment
env = gym.make("Taxi-v3", render_mode="rgb_array")  # Gymnasium auto-selects modern render backend
state, info = env.reset()

state_space = env.observation_space.n
action_space = env.action_space.n

print("State space:", state_space)
print("Action space:", action_space)

# Step 2: Initialize Q-table
Q = np.zeros((state_space, action_space))

# Step 3: Set Hyperparameters
alpha = 0.7
gamma = 0.618
epsilon = 1.0
decay = 0.01

# Step 4: Train the Agent
for episode in range(1, 10001):
    state, info = env.reset()
    done = False
    total_rewards = 0

    while not done:
        # Epsilon-greedy action selection
        if random.uniform(0, 1) < epsilon:
            action = env.action_space.sample()  # Explore
        else:
            action = np.argmax(Q[state])        # Exploit

        next_state, reward, terminated, truncated, info = env.step(action)
        done = terminated or truncated

        # Q-learning update rule
        Q[state, action] = Q[state, action] + alpha * (
            reward + gamma * np.max(Q[next_state]) - Q[state, action]
        )

        state = next_state
        total_rewards += reward

    # Decrease epsilon
    epsilon = max(0.1, epsilon - decay)

    if episode % 1000 == 0:
        print(f"Episode: {episode}, Total Reward: {total_rewards}")

# Step 5: Evaluate the trained agent
total_epochs, total_penalties = 0, 0

for _ in range(100):
    state, info = env.reset()
    done = False
    penalties, epochs = 0, 0

    while not done:
        action = np.argmax(Q[state])
        state, reward, terminated, truncated, info = env.step(action)
        done = terminated or truncated

        if reward == -10:
            penalties += 1
        epochs += 1

    total_penalties += penalties
    total_epochs += epochs

print("\nTraining finished.\n")
print("Average Timesteps per Episode:", total_epochs / 100)
print("Average Penalties per Episode:", total_penalties / 100)
