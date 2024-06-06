import random

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
        choice = int(input(f"{self.name}, enter your choice \n1.Rock\n2.Paper\n3.Scissors\n: "))
        while choice not in [1, 2, 3]:
            choice = int(input("Invalid choice.\n1.Rock\n2.Paper\n3.Scissors\n: "))

        match choice:
            case 1:
                choice = "Rock"
            case 2:
                choice = "Paper"
            case 3:
                choice = "Scissors"
            case _:
                choice = None

        
        self.choice = choice

class Computer(Player):
    def do_choice(self):
        self.choice = random.choice(["Rock", "Paper", "Scissors"])
        print(f"{self.name} chose: {self.choice}")
