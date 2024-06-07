import csv
import numpy as np
from game.player import HumanPlayer, Computer

class Game:
    def __init__(self):
        self.player = HumanPlayer("Human")
        self.computer = Computer("Computer")
        self.history_file = 'history.csv'

    def determine_winner(self):
        rules = {
            "Rock": "Scissors",
            "Paper": "Rock",
            "Scissors": "Paper"
        }

        if self.player.choice == self.computer.choice:
            return "It's a tie!"
        elif rules[self.player.choice] == self.computer.choice:
            self.computer.lose_life()
            return "Player wins this round!"
        else:
            self.player.lose_life()
            return "Computer wins this round!"

    def start(self):
        self.load_history()
        while self.player.lives > 0 and self.computer.lives > 0:
            player_result = self.player.do_choice()
            if player_result == "Thanks for playing!":
                print(player_result)
                break
            self.computer.do_choice()
            result = self.determine_winner()
            print(result)
            self.computer.record_choice(self.player.choice)
            self.save_history(self.player.choice, self.computer.choice, result)
            print(f"{self.player.name} has {self.player.lives} lives left.")
            print(f"{self.computer.name} has {self.computer.lives} lives left.")
        
        if self.player.lives == 0:
            print("Computer wins the game!")
        elif self.computer.lives == 0:
            print("Player wins the game!")

    def save_history(self, player_choice, computer_choice, result):
        with open(self.history_file, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([player_choice, computer_choice, result])

    def load_history(self):
        try:
            with open(self.history_file, 'r') as file:
                reader = csv.reader(file)
                self.computer.history = np.array(list(reader))
        except FileNotFoundError:
            self.computer.history = np.array([], dtype=str).reshape(0, 2)
