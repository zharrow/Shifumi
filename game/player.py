import random
import numpy as np

class Player:
    def __init__(self, name):
        self.name = name
        self.choice = None
        self.lives = 3

    def do_choice(self):
        pass

    def lose_life(self):
        self.lives -= 1

class HumanPlayer(Player):
    def do_choice(self):
        user_input = int(input(f"{self.name}, enter your choice: Rock(1) Paper(2) Scissors(3). Press (9) to quit: "))
        while user_input not in [1, 2, 3, 9]:
            user_input = int(input("Invalid choice.. Enter Rock(1) Paper(2) Scissors(3). Press (9) to quit: "))

        if user_input == 9:
            return "Thanks for playing!"

        choices_map = {1: "Rock", 2: "Paper", 3: "Scissors"}
        self.choice = choices_map.get(user_input, None)

class Computer(Player):
    def __init__(self, name):
        super().__init__(name)
        self.history = np.array([], dtype=str).reshape(0, 2)  # Initialize as an empty 2-column array

    def do_choice(self):
        if self.history.size > 0:
            self.choice = self.predict_choice()
        else:
            self.choice = random.choice(["Rock", "Paper", "Scissors"])
        print(f"{self.name} chose: {self.choice}")

    def predict_choice(self):
        player_choices = self.history[:, 0]
        if player_choices.size > 0:
            unique, counts = np.unique(player_choices, return_counts=True)
            most_common_choice = unique[np.argmax(counts)]
            counter_choices = {"Rock": "Paper", "Paper": "Scissors", "Scissors": "Rock"}
            return counter_choices[most_common_choice]
        else:
            return random.choice(["Rock", "Paper", "Scissors"])

    def record_choice(self, player_choice):
        self.history = np.vstack([self.history, [player_choice, self.choice]])
