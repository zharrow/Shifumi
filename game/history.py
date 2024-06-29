import pandas as pd

class History:
    def __init__(self, file_path='data/history.csv'):
        self.file_path = file_path
        self.columns = ['PlayerChoice', 'ComputerChoice', 'Result']
        self.current_game = pd.DataFrame(columns=self.columns)
        try:
            self.data = pd.read_csv(self.file_path)
        except FileNotFoundError:
            self.data = pd.DataFrame(columns=self.columns)

    def save_round(self, player_choice, computer_choice, result):
        new_row = pd.DataFrame({'PlayerChoice': [player_choice], 'ComputerChoice': [computer_choice], 'Result': [result]})
        self.current_game = pd.concat([self.current_game, new_row], ignore_index=True)

    def save_history(self):
        self.data = pd.concat([self.data, self.current_game], ignore_index=True)
        self.data.to_csv(self.file_path, index=False)

    def load_history(self):
        try:
            self.data = pd.read_csv(self.file_path)
        except FileNotFoundError:
            self.data = pd.DataFrame(columns=self.columns)

    def get_history(self):
        return self.data
