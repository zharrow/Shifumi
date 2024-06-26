import pandas as pd
from game.human import HumanPlayer
from game.computer import Computer
from game.history import History

class Game:
    def __init__(self):
        self.player = HumanPlayer("Human")
        self.computer = Computer("Computer")
        self.history = History()

    def determine_winner(self):
        rules = {
            1: 3,
            2: 1,
            3: 2
        }

        result = []
        if self.player.choice == self.computer.choice:
            result = [0, "It's a tie!"]
        elif rules[self.player.choice] == self.computer.choice:
            self.computer.lose_life()
            result = [1, "Player wins this round!"]
        else:
            self.player.lose_life()
            result = [-1, "Computer wins this round!"]

        self.history.save_round(self.player.choice, self.computer.choice, result[0])
        
        return result[1]

    def startConsole(self):
        self.history.load_history()
        while self.player.lives > 0 and self.computer.lives > 0:
            player_result = self.player.do_choice()
            if player_result == "Thanks for playing!":
                print(player_result)
                break
            self.computer.do_choice()
            result = self.determine_winner()
            print(result)
            self.computer.record_choice(self.player.choice)
            self.history.save_round(self.player.choice, self.computer.choice, result)
            print(f"{self.player.name} has {self.player.lives} lives left.")
            print(f"{self.computer.name} has {self.computer.lives} lives left.")
        
        if self.player.lives == 0:
            print("Computer wins the game!")
        elif self.computer.lives == 0:
            print("Player wins the game!")
