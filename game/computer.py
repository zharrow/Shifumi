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
        patterns = self.find_patterns(current_game, history)
        self.choice = self.predict_choice_from_patterns(patterns)

    def find_patterns(self, current_game: pd.DataFrame, history: pd.DataFrame):
        cgl: list = current_game[:].values.tolist()
        histl: list = history[:].values.tolist()
        patterns = []

        for i in range(0, len(histl)-1):
            for j in range(len(cgl), 0, -1):
                if cgl[:j] == histl[i:i+j]:
                    if i+j < len(histl)-1:
                        patterns.append(histl[i+j+1])

        return patterns

    def predict_choice_from_patterns(self, patterns):
        rules = {
            1: 2,
            2: 3,
            3: 1
        }

        choice = None
        patterns_percentage = self.calculate_percentage(patterns)
        pattern_chosen = None

        while choice == None:
            if pattern_chosen == None:
                pattern_chosen = self.select_pattern(patterns_percentage)
            else: 
                print(f"Pop pattern: {pattern_chosen}")
                patterns_percentage.pop(f"{pattern_chosen[0]}, {pattern_chosen[1]}, {pattern_chosen[2]}")
                pattern_chosen = self.select_pattern(patterns_percentage)

            choice = self.determine_choice(pattern_chosen, rules)

        print(f"Patterns: {patterns}")
        print(f"Patterns percentage: {patterns_percentage}")
        print(f"Pattern chosen: {pattern_chosen}")
        print(f"Predicted choice: {choice}")

        return choice
    
    def calculate_percentage(self, patterns):
        patterns_percentage = {}

        if len(patterns) > 0:
            for _, pattern in enumerate(patterns):
                patterns_percentage.update({f"{pattern[0]}, {pattern[1]}, {pattern[2]}": patterns.count(pattern) / len(patterns)})

        return patterns_percentage

    def select_pattern(self, patterns_percentage):
        pattern_chosen = None

        if len(patterns_percentage) > 0:
            for pattern in patterns_percentage:
                if pattern_chosen == None:
                    pattern_chosen = pattern
                if patterns_percentage[pattern] >= patterns_percentage[pattern_chosen]:
                    if len(pattern.split(", ")) > len(pattern_chosen.split(", ")):
                        pattern_chosen = pattern
                    pattern_chosen = pattern

        return pattern_chosen

    def determine_choice(self, pattern_chosen, rules):
        choice = None

        if pattern_chosen != None:
            pattern_chosen = pattern_chosen.split(", ")
            pattern_chosen = [int(i) for i in pattern_chosen]
            if pattern_chosen[2] == -1:
                choice = pattern_chosen[1]
            elif pattern_chosen[2] == 1:
                choice = rules[pattern_chosen[0]]
        else:
            print(f"Random choice")
            choice = random.choice([1, 2, 3])

        if choice == None:
            print(f"Random choice")
            choice = random.choice([1, 2, 3])

        return choice

    def record_choice(self, player_choice):
        self.history = np.vstack([self.history, [player_choice, self.choice]])
