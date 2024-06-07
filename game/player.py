import random
import numpy as np
import pandas as pd

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
        # dfExport = pd.DataFrame({"A": [1, 2, 3], "B": [1, 2, 3], "C": [1, 2, 3] },index=['Player', 'Computer', 'Result'])
        # print(dfExport)
        # dfImport = pd.read_csv('history.csv')

    def do_choice(self):
        choices = ["Rock", "Paper", "Scissors"]
        choice = np.random.choice(choices)
        print(f"{self.name} chose: {choice}")

        self.choice = choice
