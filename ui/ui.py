import tkinter as tk
import os
from game.game import Game

class Canvas(tk.Canvas):
    def __init__(self, master, w=None, h=None):
        tk.Canvas.__init__(self, master)
        self.configure(width=w, height=h)
        self.configure(bg= 'yellow')
        self.create_text(w/2, h/2, text= 'Ceci est un canvas:\nUne zone de dession ou \n une zone de jeu.', font= ('Calibri', 30, 'bold'), fill= 'orange')

class Button(tk.Button):
    def __init__(self, master, fn, text, id=None):
        self.id = id
        self.text = text
        self.fn = fn
        tk.Button.__init__(self, master, text= self.text)
        self.configure(width=20, height=2)
        self.configure(bg= 'green', fg='white')
        self.configure(font= ('Times New Roman', 20, 'italic'))
        self.configure(command= self.function)

    def function(self):
        if (self.id == None):
            self.fn()
        elif (type(self.id) == bool):
            self.fn(self.id)
        else:
            self.fn(self.id)

class Frame(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master, width=100, height=100)
        self.configure(bg= 'pink')

        def restart_game():
            master.restart_button.destroy()
            master.start_game(restart=True)

        def winner(winner):
            master.round_result.configure(text=f"Round result: {winner} wins the game!")
            master.restart_button = Button(master, restart_game, "Restart the game")
            master.restart_button.grid(row=6, column=0, padx=20, pady=20)
            master.leave_button.grid(row=6, column=1, padx=20, pady=20)

            self.destroy()

        def choice(i):
            rules = {
                1: "Rock",
                2: "Paper",
                3: "Scissors"
            }

            master.game.player.do_choice_interface(i)
            master.player_choice.configure(text=f"{master.game.player.name} choice: {rules[master.game.player.choice]}")

            master.game.computer.do_choice()
            master.computer_choice.configure(text=f"Computer choice: {rules[master.game.computer.choice]}")

            roundResult = master.game.determine_winner()
            master.round_result.configure(text=f"Round result: {roundResult}")

            master.player_lives.configure(text=f"{master.game.player.name} lives: {master.game.player.lives}")
            master.computer_lives.configure(text=f"Computer lives: {master.game.computer.lives}")

            if master.game.player.lives <= 0:
                winner("Computer")
            elif master.game.computer.lives <= 0:
                winner(master.game.player.name)


        self.button_list = [Button(self, choice, id, i+1) for i, id in enumerate(['Rock', 'Paper', 'Scissors'])]
        for k, button in enumerate(self.button_list):
            button.grid(row=0, column=k, padx=20, pady=20)

class Label(tk.Label):
    def __init__(self, master,  t=None, width=20, height=2, textSize=30):
        tk.Label.__init__(self, master, width=width, height=height)
        self.configure(text= t)
        self.configure(bg= 'grey', fg= 'black')
        self.configure(font= ('Arial', textSize))

class Tk(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.configure(bg= 'light blue')
        #self.state('zoomed')
        self.geometry('1000x800+400+0')
        self.title = Label(self, t= "Shifumi Game")
        self.title.grid(row=0, column=0, columnspan=3, padx=20, pady=20)

        self.label = Label(self, t="Enter your name (optional):", textSize=15, width=25)
        self.label.grid(row=1, column=0, padx=5, pady=5)

        self.entry = tk.Entry(self)
        self.entry.grid(row=1, column=1, padx=5, pady=5)

        self.start_button = Button(self, self.start_game, "Start the game")
        self.start_button.grid(row=2, column=0, columnspan=2, padx=20, pady=20)

        self.leave_button = Button(self, self.stop_game, "Leave the game")
        self.leave_button.grid(row=3, column=0, columnspan=3, padx=20, pady=20)

    def start_game(self, restart=False):
        if restart == False:
            self.player_name = self.entry.get()

        self.game = Game(self.player_name)

        self.start_button.destroy()
        self.label.destroy()
        self.entry.destroy()

        self.menu = Frame(self)
        self.menu.grid(row=2, column=0, columnspan=3, padx=10, pady=10)

        self.player_lives = Label(self, t=f"{self.game.player.name} lives: {self.game.player.lives}", textSize=15, width=25)
        self.player_lives.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

        self.player_choice = Label(self, t=f"{self.game.player.name} choice: ", textSize=15, width=25)
        self.player_choice.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

        self.computer_lives = Label(self, t=f"Computer lives: {self.game.computer.lives}", textSize=15, width=25)
        self.computer_lives.grid(row=3, column=1, columnspan=2, padx=10, pady=10)

        self.computer_choice = Label(self, t=f"Computer choice: ", textSize=15, width=25)
        self.computer_choice.grid(row=4, column=1, columnspan=2, padx=10, pady=10)

        self.round_result = Label(self, t="Round result: ", textSize=15, width=40)
        self.round_result.grid(row=5, column=0, columnspan=3, padx=10, pady=10)

        self.leave_button.grid(row=6, column=0, padx=20, pady=20)

    def stop_game(self):
        self.quit()
