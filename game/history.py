import pandas as pd

class History:
    def __init__(self, file_path='data/history.csv'):
        self.file_path = file_path
        self.columns = ['PlayerChoice', 'ComputerChoice', 'Result']
        try:
            self.data = pd.read_csv(self.file_path)
        except FileNotFoundError:
            self.data = pd.DataFrame(columns=self.columns)

    def save_round(self, player_choice, computer_choice, result):
        new_entry = pd.DataFrame([[player_choice, computer_choice, result]], columns=self.columns)
        self.data = pd.concat([self.data, new_entry], ignore_index=True)
        self.data.to_csv(self.file_path, index=False)

    def load_history(self):
        try:
            self.data = pd.read_csv(self.file_path)
        except FileNotFoundError:
            self.data = pd.DataFrame(columns=self.columns)

    def get_history(self):
        return self.data
