from game.player import Player

class HumanPlayer(Player):
    def do_choice_interface(self, user_input):
        self.choice = user_input

    def do_choice_console(self):
        user_input = int(input(f"{self.name}, enter your choice: Rock(1) Paper(2) Scissors(3). Press (9) to quit: "))
        while user_input not in [1, 2, 3, 9]:
            user_input = int(input("Invalid choice.. Enter Rock(1) Paper(2) Scissors(3). Press (9) to quit: "))

        if user_input == 9:
            return "Thanks for playing!"

        self.choice = user_input
