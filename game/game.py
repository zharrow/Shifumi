from game.player import HumanPlayer, Computer

class Game:
    def __init__(self):
        self.player = HumanPlayer("Human")
        self.computer = Computer("IA")

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
            self.player.do_choice()
            self.computer.do_choice()
            result = self.determine_winner()
            print(result)
            print(f"{self.player.name} has {self.player.lives} lives left.")
            print(f"{self.computer.name} has {self.computer.lives} lives left.")
            print("\n")
        
        if self.player.lives == 0:
            print("Computer wins the game!")
        else:
            print("Player wins the game!")
