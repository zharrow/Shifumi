class Player:
    def __init__(self, name):
        self.name = name
        self.choice = None
        self.lives = 3

    def do_choice(self):
        pass

    def lose_life(self):
        self.lives -= 1

class Human(Player):
    def do_choice_interface(self, user_input):
        self.choice = user_input

    def do_choice_console(self):
        user_input = int(input(f"{self.name}, enter your choice: Rock(1) Paper(2) Scissors(3). Press (9) to quit: "))
        while user_input not in [1, 2, 3, 9]:
            user_input = int(input("Invalid choice.. Enter Rock(1) Paper(2) Scissors(3). Press (9) to quit: "))

        if user_input == 9:
            return "Thanks for playing!"

        self.choice = user_input

class Computer(Player):
    def __init__(self, name):
        super().__init__(name)
        # dfExport = pd.DataFrame({"A": [1, 2, 3], "B": [1, 2, 3], "C": [1, 2, 3] },index=['Player', 'Computer', 'Result'])
        # print(dfExport)
        # dfImport = pd.read_csv('history.csv')

    def do_choice(self):
        choices = [1, 2, 3]
        choice = np.random.choice(choices)

        self.choice = choice
