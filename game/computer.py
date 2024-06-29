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
        cgl = current_game[:].values.tolist()
        histl = history[:].values.tolist()
        patterns = []

        for i in range(0, len(histl)):
            for j in range(len(cgl), 1, -1):
                if cgl == histl[i:i+j]:
                    patterns.append(histl[i+j+1])
                    break

            if patterns:
                break

        return patterns

    def predict_choice_from_patterns(self, patterns):
        choice = 0
        rules = {
            1: 2,
            2: 3,
            3: 1
        }

        if len(patterns) > 0:
            for index, pattern in enumerate(patterns):
                print(f"Pattern {index}: {pattern}")
                if pattern[2] == -1:
                    choice = pattern[1]
                elif pattern[2] == 1:
                    choice = rules[pattern[0]]
                else:
                    choice = random.choice([1, 2, 3])
                    # TODO: Ajouter un choix plus complexe s'il y a une égalité
        else:
            choice = random.choice([1, 2, 3])

        print(f"Predicted choice: {choice}")

        return choice
            

    

    def gpt_find_patterns(self, current_game, history):        
        # Convertir les choix en listes pour la comparaison
        current_choices = current_game[['PlayerChoice', 'ComputerChoice', 'Result']].values.tolist()
        pattern_length = len(current_choices)
        
        # Liste pour stocker les choix suivants
        next_choices = []
        
        # Comparer les séquences de l'historique avec les choix actuels
        for i in range(len(history) - pattern_length):
            historical_pattern = history[['PlayerChoice', 'ComputerChoice', 'Result']].iloc[i:i+pattern_length].values.tolist()
            if historical_pattern == current_choices:
                if i + pattern_length < len(history):
                    next_choices.append(history['PlayerChoice'].iloc[i + pattern_length])

        print(f"Next choices: {next_choices}")
        
        # Si des séquences sont trouvées, prédire le prochain coup basé sur la fréquence
        if next_choices:
            next_choice = self.gpt_predict_from_sequences(next_choices)
        else:
            # Sinon, choisir aléatoirement
            next_choice = np.random.choice(self.choices)
        
        return next_choice

    def gpt_predict_from_sequences(self, sequences):
        # Calculer la fréquence des choix suivants
        freq = pd.Series(sequences).value_counts(normalize=True)
        
        # Choisir en fonction des fréquences
        next_choice = np.random.choice(freq.index, p=freq.values)
        return next_choice

    def record_choice(self, player_choice):
        self.history = np.vstack([self.history, [player_choice, self.choice]])
