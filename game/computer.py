import random
import numpy as np
from game.player import Player

class Computer(Player):
    def __init__(self, name):
        super().__init__(name)
        self.history = np.array([], dtype=str).reshape(0, 2)  # Initialize as an empty 2-column array

    def do_choice(self):
        if self.history.size > 0:
            self.choice = self.predict_choice()
        else:
            self.choice = random.choice([1, 2, 3])
        print(f"{self.name} chose: {self.choice}")

    def predict_choice(self):
        player_choices = self.history[:, 0]
        if player_choices.size > 0:
            unique, counts = np.unique(player_choices, return_counts=True)
            most_common_choice = unique[np.argmax(counts)]
            counter_choices = {1: 2, 2: 3, 3: 1}
            return counter_choices[most_common_choice]
        else:
            return random.choice([1, 2, 3])

    def record_choice(self, player_choice):
        self.history = np.vstack([self.history, [player_choice, self.choice]])
