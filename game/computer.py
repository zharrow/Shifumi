import random
import numpy as np
import pandas as pd
from game.player import Player

class Computer(Player):
    def __init__(self, name):
        super().__init__(name)
        self.choices = [1, 2, 3]

    def do_choice(self):
        if self.history.size > 0:
            self.choice = self.predict_choice()
        else:
            self.choice = random.choice([1, 2, 3])
        print(f"{self.name} chose: {self.choice}")

    def predict_choice(self, current_game, history):
        self.choice = 0

        patterns = self.find_patterns(current_game, history)
        self.choice = self.predict_choice_from_patterns(patterns)

    def find_patterns(self, current_game: pd.DataFrame, history: pd.DataFrame):
        cgl: list = current_game[:].values.tolist()
        histl: list = history[:].values.tolist()
        patterns = []

        for i in range(0, len(histl)-1):
            for j in range(len(cgl), 0, -1):
                if cgl == histl[i:i+j]:
                    if i+j < len(histl)-1:
                        patterns.append(histl[i+j+1])

        return patterns

    def predict_choice_from_patterns(self, patterns):
        choice = 0

        patterns_percentage = {}
        pattern_chosen = None

        rules = {
            1: 2,
            2: 3,
            3: 1
        }

        if len(patterns) > 0:
            for _, pattern in enumerate(patterns):
                choice = pattern[1]
                patterns_percentage.update({f"{pattern[0]}, {pattern[1]}, {pattern[2]}": patterns.count(pattern) / len(patterns)})

        if len(patterns_percentage) > 0:
            for pattern in patterns_percentage:
                if pattern_chosen == None:
                    pattern_chosen = pattern
                if patterns_percentage[pattern] >= patterns_percentage[pattern_chosen]:
                    pattern_chosen = pattern            

        if pattern_chosen != None:
            pattern_chosen = pattern_chosen.split(", ")
            pattern_chosen = [int(i) for i in pattern_chosen]
            if pattern_chosen[2] == -1:
                choice = pattern_chosen[1]
            elif pattern_chosen[2] == 1:
                choice = rules[pattern_chosen[0]]
            else:
                pass
                # TODO: Implement a better way to choose the next choice

        #print(f"Patterns: {patterns}")
        #print(f"Patterns percentage: {patterns_percentage}")
        #print(f"Pattern chosen: {pattern_chosen}")
        #print(f"Predicted choice: {choice}")

        if choice == 0:
            choice = random.choice([1, 2, 3])

        return choice

    def record_choice(self, player_choice):
        self.history = np.vstack([self.history, [player_choice, self.choice]])
