import time
import random

class SimpleAgent:
    def __init__(self, environment):
        self.environment = environment
        self.goal = "find_treasure"
        self.location = (0, 0) # Starting location

    def perceive(self):
        return self.environment.get_state(self.location)

    def decide(self, perception):
        possible_actions = ["move_north", "move_south", "move_east", "move_west"]
        if "treasure" in perception:
            return "found_treasure"
        return random.choice(possible_actions)

    def act(self, action):
        print(f"Agent at {self.location} performing: {action}")
        if action == "move_north":
            self.location = (self.location[0], self.location[1] + 1)
        elif action == "move_south":
            self.location = (self.location[0], self.location[1] - 1)
        elif action == "move_east":
            self.location = (self.location[0] + 1, self.location[1])
        elif action == "move_west":
            self.location = (self.location[0] - 1, self.location[1])
        time.sleep(0.5)

    def learn(self, reward):
        # Very basic "learning" - just printing feedback
        print(f"Received reward: {reward}")

    def run(self, max_steps=10):
        for _ in range(max_steps):
            perception = self.perceive()
            action = self.decide(perception)
            if action == "found_treasure":
                print("Agent found the treasure!")
                break
            self.act(action)
            reward = self.environment.get_reward(self.location, self.goal)
            self.learn(reward)
        else:
            print("Agent failed to find the treasure within the time limit.")

class SimpleEnvironment:
    def __init__(self, treasure_location):
        self.treasure_location = treasure_location

    def get_state(self, location):
        if location == self.treasure_location:
            return ["treasure"]
        return []

    def get_reward(self, location, goal):
        if location == self.treasure_location and goal == "find_treasure":
            return 10
        return -0.1 # Small negative reward for moving

# Example usage
treasure_location = (2, 1)
env = SimpleEnvironment(treasure_location)
agent = SimpleAgent(env)
agent.run(max_steps=20)
