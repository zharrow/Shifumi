class Player:
    def __init__(self, name):
        self.name = name
        self.choice = None
        self.lives = 3

    def do_choice(self):
        pass

    def lose_life(self):
        self.lives -= 1