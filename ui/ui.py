import tkinter as tk
from game.game import Game
import matplotlib.pyplot as plt
import pandas as pd

class CustomButton(tk.Button):
    def __init__(self, master, fn, text, id=None):
        super().__init__(master, text=text, width=20, height=2, bg='green', fg='white', font=('Times New Roman', 20, 'italic'))
        self.id = id
        self.fn = fn
        self.config(command=self.function)

    def function(self):
        if self.id is None:
            self.fn()
        else:
            self.fn(self.id)

class CustomLabel(tk.Label):
    def __init__(self, master, text=None, width=20, height=2, textSize=30):
        super().__init__(master, text=text, width=width, height=height, bg='grey', fg='black', font=('Arial', textSize))

class MainMenuFrame(tk.Frame):
    def __init__(self, master, switch_frame):
        super().__init__(master)
        self.switch_frame = switch_frame
        self.create_widgets(master)

    def create_widgets(self, master):
        self.title_label = CustomLabel(self, text="Shifumi Game", textSize=30, width=40)
        self.title_label.grid(row=0, column=0, columnspan=3, padx=20, pady=20)
        self.start_button = CustomButton(self, lambda: self.switch_frame("game"), "Start the game")
        self.start_button.grid(row=2, column=0, columnspan=3, padx=20, pady=20)
        self.stat_button = CustomButton(self, lambda: self.switch_frame("stats"), "Statistics")
        self.stat_button.grid(row=3, column=0, columnspan=3, padx=20, pady=20)
        self.leave_button = CustomButton(self, master.quit, "Leave the game")
        self.leave_button.grid(row=4, column=0, columnspan=3, padx=20, pady=20)

class GameFrame(tk.Frame):
    def __init__(self, master, switch_frame):
        super().__init__(master)
        self.switch_frame = switch_frame
        self.game = Game()
        self.create_widgets()

    def create_widgets(self):
        self.menu_frame = tk.Frame(self, width=90, height=100, bg='pink')
        self.menu_frame.grid(row=2, column=0, columnspan=4, padx=10, pady=10)
        self.button_list = [CustomButton(self.menu_frame, self.choice, text, i+1) for i, text in enumerate(['Rock', 'Paper', 'Scissors'])]
        for k, button in enumerate(self.button_list):
            button.grid(row=0, column=k, padx=10, pady=10)

        self.player_lives = CustomLabel(self, text=f"Human lives: {self.game.player.lives}", textSize=15, width=25)
        self.player_lives.grid(row=3, column=0, columnspan=2, padx=10, pady=10)
        self.player_choice = CustomLabel(self, text=f"Human choice: ", textSize=15, width=25)
        self.player_choice.grid(row=4, column=0, columnspan=2, padx=10, pady=10)
        self.computer_lives = CustomLabel(self, text=f"Computer lives: {self.game.computer.lives}", textSize=15, width=25)
        self.computer_lives.grid(row=3, column=1, columnspan=2, padx=10, pady=10)
        self.computer_choice = CustomLabel(self, text="Computer choice: ", textSize=15, width=25)
        self.computer_choice.grid(row=4, column=1, columnspan=2, padx=10, pady=10)
        self.round_result = CustomLabel(self, text="Round result: ", textSize=15, width=40)
        self.round_result.grid(row=5, column=0, columnspan=4, padx=10, pady=10)
        self.leave_button = CustomButton(self, lambda: self.switch_frame("main_menu"), "Main menu")
        self.leave_button.grid(row=6, column=0, padx=20, pady=20)

    def choice(self, i):
        rules = {1: "Rock", 2: "Paper", 3: "Scissors"}
        self.game.player.do_choice_interface(i)
        self.player_choice.config(text=f"{self.game.player.name} choice: {rules[self.game.player.choice]}")
        self.game.computer.predict_choice(self.game.history.current_game, self.game.history.data)
        self.computer_choice.config(text=f"Computer choice: {rules[self.game.computer.choice]}")
        roundResult = self.game.determine_winner()
        self.round_result.config(text=f"Round result: {roundResult}")
        self.update_lives()
        if self.game.player.lives <= 0:
            self.game.history.save_history()
            self.switch_frame("result", "Computer")
        elif self.game.computer.lives <= 0:
            self.game.history.save_history()
            self.switch_frame("result", "Human")

    def update_lives(self):
        self.player_lives.config(text=f"Human lives: {self.game.player.lives}")
        self.computer_lives.config(text=f"Computer lives: {self.game.computer.lives}")

class ResultFrame(tk.Frame):
    def __init__(self, master, switch_frame, winner):
        super().__init__(master)
        self.switch_frame = switch_frame
        self.winner = winner
        self.create_widgets()

    def create_widgets(self):
        result_label = CustomLabel(self, text=f"{self.winner} wins the game!", textSize=30, width=40)
        result_label.grid(row=0, column=0, columnspan=3, padx=20, pady=20)
        restart_button = CustomButton(self, lambda: self.switch_frame("game"), "Restart the game")
        restart_button.grid(row=1, column=0, columnspan=3, padx=20, pady=20)
        main_menu_button = CustomButton(self, lambda: self.switch_frame("main_menu"), "Main menu")
        main_menu_button.grid(row=2, column=0, columnspan=3, padx=20, pady=20)
        leave_button = CustomButton(self, self.quit, "Leave the game")
        leave_button.grid(row=3, column=0, columnspan=3, padx=20, pady=20)

class StatsFrame(tk.Frame):
    def __init__(self, master, switch_frame):
        super().__init__(master)
        self.switch_frame = switch_frame
        self.create_widgets()
        self.display_statistics()

    def create_widgets(self):
        self.title_label = CustomLabel(self, text="Game Statistics", textSize=30, width=40)
        self.title_label.grid(row=0, column=0, columnspan=3, padx=20, pady=20)
        self.back_button = CustomButton(self, lambda: self.switch_frame("main_menu"), "Back to Main Menu")
        self.back_button.grid(row=1, column=0, columnspan=3, padx=20, pady=20)
        self.figure_frame = tk.Frame(self)
        self.figure_frame.grid(row=2, column=0, columnspan=3, padx=20, pady=20)

    def display_statistics(self):
        df = pd.read_csv('data/history.csv')
        history: list = df[:].values.tolist()

        player = []
        computer = []
        draw = []

        for i, row in enumerate(history):
            if row[2] == 1:
                player.append(row)
            elif row[2] == -1:
                computer.append(row)
            else:
                draw.append(row)

        total_games = len(history)
        player_wins = len(player)
        computer_wins = len(computer)
        draws = len(draw)

        player_win_percentage = (player_wins / total_games) * 100
        computer_win_percentage = (computer_wins / total_games) * 100
        draw_percentage = (draws / total_games) * 100

        labels = ['Player wins', 'Computer wins', 'Draws']
        percentages = [player_win_percentage, computer_win_percentage, draw_percentage]
        colors = ['red', 'blue', 'green']
        plt.bar(labels, percentages, color=colors)
        plt.xlabel('Categories')
        plt.ylabel('Percentage')
        plt.title('Game Statistics')
        plt.show()

class MainApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.configure(bg='light blue')
        self.geometry('925x477+400+0')
        self.frames = {}
        self.show_frame("main_menu")

    def show_frame(self, frame_name, winner=None):
        frame = self.frames.get(frame_name)
        if frame:
            frame.destroy()
        if frame_name == "main_menu":
            frame = MainMenuFrame(self, self.show_frame)
        elif frame_name == "game":
            frame = GameFrame(self, self.show_frame)
        elif frame_name == "result":
            frame = ResultFrame(self, self.show_frame, winner)
        elif frame_name == "stats":
            frame = StatsFrame(self, self.show_frame)
        self.frames[frame_name] = frame
        frame.grid(row=0, column=0, sticky="nsew")