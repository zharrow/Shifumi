from game.player import Player

class HumanPlayer(Player):
    def do_choice(self):
        user_input = int(input(f"{self.name}, enter your choice: Rock(1) Paper(2) Scissors(3). Press (9) to quit: "))
        while user_input not in [1, 2, 3, 9]:
            user_input = int(input("Invalid choice.. Enter Rock(1) Paper(2) Scissors(3). Press (9) to quit: "))

        if user_input == 9:
            return "Thanks for playing!"

        choices_map = {1: "Rock", 2: "Paper", 3: "Scissors"}
        self.choice = choices_map.get(user_input, None)
