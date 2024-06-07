import csv
import numpy as np
from game.player import HumanPlayer, Computer

class Game:
    def __init__(self):
        self.player = HumanPlayer("Human")
        self.computer = Computer("Computer")

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
        while self.player.lives > 0 and self.computer.lives > 0:
            player_result = self.player.do_choice()
            if player_result == "Thanks for playing!":
                print(player_result)
                break
            self.computer.do_choice()
            result = self.determine_winner()
            print(result)
            print(f"{self.player.name} has {self.player.lives} lives left.")
            print(f"{self.computer.name} has {self.computer.lives} lives left.\n")
        
        if self.player.lives == 0:
            print("Computer wins the game!")
        elif self.computer.lives == 0:
            print("Player wins the game!")
