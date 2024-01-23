# Import modules(built-in)
from tkinter import *
import tkinter.messagebox
import pickle
import random
import time
import os

gamedata = {}

def gamedata_read():
    global gamedata
    load_file = open('gamedata.dat', 'rb')
    gamedata = pickle.load(load_file)
    load_file.close()
    return gamedata

def gamedata_write(data:dict):
    save_file = open('gamedata.dat', 'wb')
    pickle.dump(gamedata, save_file)
    save_file.close()

def gamedata_delete():
    if tkinter.messagebox.askokcancel("Delete Anyway", "If you do this, your game data will be deleted forever. You can not undo this. Are you sure you want to delete it?"):
        save_file = open('gamedata.dat', 'wb')
        gamedata = {
            'game-played': 0,
            'rock-win': 0,
            'paper-win': 0,
            'scissor-win': 0
        }
        pickle.dump(gamedata, save_file)
        save_file.close()
    else:
        return 

if os.path.exists('gamedata.dat'):
    gamedata_read()

else:
    save_file = open('gamedata.dat', 'wb+')
    gamedata = {
        'game-played': 0,
        'rock-win': 0,
        'paper-win': 0,
        'scissor-win': 0
    }
    pickle.dump(gamedata, save_file)
    save_file.close()

base_dir = os.path.dirname(__file__)

# Not built-in(Need to install)
import matplotlib.pyplot as plt

GAMING = True
time_start = time.time()

# Initialize Game
class Game:
    def __init__(self):
        tk = Tk()
        self.tk = tk
        self.tk.title("Rock vs Paper vs Scissor(BETA1.1)")
        self.canvas = Canvas(tk, width=1200, height=850, background='grey')
        self.canvas.pack()

# Initialize three 'competitors'
class Rock:
    def __init__(self, canvas, x, y, speed, i_x, i_y):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.pos = [self.x, self.y]
        file_path = os.path.join(base_dir, './rock.png')
        self.images = PhotoImage(file=file_path) # Image size 55px*55px
        self.image = self.canvas.create_image(self.x, self.y, anchor='nw', image=self.images)
        # Get random speed
        self.speed = speed
        self.x = i_x
        self.y = i_y
    def draw(self):
        self.canvas.move(self.image, self.x, self.y)
        self.pos = self.canvas.coords(self.image)
        # Detect if it touches the edge of the canvas
        if self.pos[0] <= 0:
            self.x = self.speed
        if self.pos[1] <= 0:
            self.y = self.speed
        if self.pos[0] + 55 >= self.canvas.winfo_reqwidth():
            self.x = -self.speed
        if self.pos[1] + 55 >= self.canvas.winfo_reqheight() - 155:
            self.y = -self.speed

    def fight(self):
        papers_pos = []
        for a in papers:
            papers_pos.append(a.pos)
        
        for pos_x, pos_y in papers_pos: # Rock versus Paper = Die
            # Detect if it touches its component
            if self.pos[0] <= pos_x <= self.pos[0]+55 and self.pos[1] <= pos_y <= self.pos[1]+55 \
            or self.pos[0] <= pos_x+55 <= self.pos[0]+55 and self.pos[1] <= pos_y <= self.pos[1]+55 \
            or self.pos[0] <= pos_x <= self.pos[0]+55 and self.pos[1] <= pos_y+55 <= self.pos[1]+55 \
            or self.pos[0] <= pos_x+55 <= self.pos[0]+55 and self.pos[1] <= pos_y+55 <= self.pos[1]+55:
                papers.append(Paper(game.canvas, self.pos[0], self.pos[1], round(random.uniform(0.5, 4), 2), round(random.uniform(-4, 4), 2), round(random.uniform(-4, 4), 2)))
                rocks.remove(self) # Die
                del(self)
                return 0

class Paper:
    def __init__(self, canvas, x, y, speed, i_x, i_y):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.pos = [self.x, self.y]
        file_path = os.path.join(base_dir, './paper.png')
        self.images = PhotoImage(file=file_path)
        self.image = self.canvas.create_image(self.x, self.y, anchor='nw', image=self.images)
        self.speed = speed
        self.x = i_x
        self.y = i_y

    def draw(self):
        self.canvas.move(self.image, self.x, self.y)
        self.pos = self.canvas.coords(self.image)
        if self.pos[0] <= 0:
            self.x = self.speed
        if self.pos[1] <= 0:
            self.y = self.speed
        if self.pos[0] + 55 >= self.canvas.winfo_reqwidth():
            self.x = -self.speed
        if self.pos[1] + 55 >= self.canvas.winfo_reqheight() - 155:
            self.y = -self.speed

    def fight(self):
        scissors_pos = []
        for a in scissors:
            scissors_pos.append(a.pos)
        
        for pos_x, pos_y in scissors_pos: # Die
            if self.pos[0] <= pos_x <= self.pos[0]+55 and self.pos[1] <= pos_y <= self.pos[1]+55 \
                or self.pos[0] <= pos_x+55 <= self.pos[0]+55 and self.pos[1] <= pos_y <= self.pos[1]+55 \
                or self.pos[0] <= pos_x <= self.pos[0]+55 and self.pos[1] <= pos_y+55 <= self.pos[1]+55 \
                or self.pos[0] <= pos_x+55 <= self.pos[0]+55 and self.pos[1] <= pos_y+55 <= self.pos[1]+55:
                    scissors.append(Scissor(game.canvas, self.pos[0], self.pos[1], round(random.uniform(0.5, 4), 2), round(random.uniform(-4, 4), 2), round(random.uniform(-4, 4), 2)))
                    papers.remove(self)
                    del(self)
                    return 0

class Scissor:
    def __init__(self, canvas, x, y, speed, i_x, i_y):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.pos = [self.x, self.y]
        file_path = os.path.join(base_dir, './scissor.png')
        self.images = PhotoImage(file=file_path)
        self.image = self.canvas.create_image(self.x, self.y, anchor='nw', image=self.images)
        self.speed = speed
        self.x = i_x
        self.y = i_y

    def draw(self):
        self.canvas.move(self.image, self.x, self.y)
        self.pos = self.canvas.coords(self.image)
        if self.pos[0] <= 0:
            self.x = self.speed
        if self.pos[1] <= 0:
            self.y = self.speed
        if self.pos[0] + 55 >= self.canvas.winfo_reqwidth():
            self.x = -self.speed
        if self.pos[1] + 55 >= self.canvas.winfo_reqheight() - 155:
            self.y = -self.speed

    def fight(self):
        rocks_pos = []
        for a in rocks:
            rocks_pos.append(a.pos)
        
        for pos_x, pos_y in rocks_pos: # Die
            if self.pos[0] <= pos_x <= self.pos[0]+55 and self.pos[1] <= pos_y <= self.pos[1]+55 \
                or self.pos[0] <= pos_x+55 <= self.pos[0]+55 and self.pos[1] <= pos_y <= self.pos[1]+55 \
                or self.pos[0] <= pos_x <= self.pos[0]+55 and self.pos[1] <= pos_y+55 <= self.pos[1]+55 \
                or self.pos[0] <= pos_x+55 <= self.pos[0]+55 and self.pos[1] <= pos_y+55 <= self.pos[1]+55:
                    rocks.append(Rock(game.canvas, self.pos[0], self.pos[1], round(random.uniform(0.5, 4), 2), round(random.uniform(-4, 4), 2), round(random.uniform(-4, 4), 2)))
                    scissors.remove(self)
                    del(self)
                    return 0

game = Game()
tk = game.tk

canvas = game.canvas
rocks = [Rock(canvas, random.randint(50,canvas.winfo_reqwidth()-50), random.randint(50, canvas.winfo_reqheight()-50), round(random.uniform(0.5, 4), 2), round(random.uniform(-4, 4), 2), round(random.uniform(-4, 4), 2)) for i in range(20)]
papers = [Paper(canvas, random.randint(50,canvas.winfo_reqwidth()-50), random.randint(50, canvas.winfo_reqheight()-50), round(random.uniform(0.5, 4), 2), round(random.uniform(-4, 4), 2), round(random.uniform(-4, 4), 2)) for i in range(20)]
scissors = [Scissor(canvas, random.randint(50,canvas.winfo_reqwidth()-50), random.randint(50, canvas.winfo_reqheight()-50), round(random.uniform(0.5, 4), 2), round(random.uniform(-4, 4), 2), round(random.uniform(-4, 4), 2)) for i in range(20)]

rocks_scoreboard = Label(tk, text="Rock:20")
rocks_scoreboard.place(x=0, y=0)
papers_scoreboard = Label(tk, text="Paper:20")
papers_scoreboard.place(x=0, y=20)
scissors_scoreboard = Label(tk, text="Scissor:20")
scissors_scoreboard.place(x=0, y=40)

winner_team = ""

def update_scoreboard(rocks_score:int, papers_score:int, scissors_score:int):
    global winner_team
    scores = [rocks_score, papers_score, scissors_score]
    scoreboards = [rocks_scoreboard, papers_scoreboard, scissors_scoreboard]
    for scoreboard_name in scoreboards:
        current_status = scoreboard_name["text"]
        text, previous_score = current_status.split(":")
        current_score = scores[scoreboards.index(scoreboard_name)]
        if current_score != 0:
            final_text = text + ":" + str(current_score)
        if current_score == 0:
            final_text = text + ":" + "Game Over"
        scoreboard_name["text"] = final_text
    try:
        winner = scoreboards[scores.index(60)]
    except ValueError:
        pass
    else:
        if scoreboards.index(winner) == 0:
            gamedata['game-played'] += 1
            gamedata['rock-win'] += 1
            gamedata_write(gamedata)
            winner_team = "Rock"
        if scoreboards.index(winner) == 1:
            gamedata['game-played'] += 1
            gamedata['paper-win'] += 1
            gamedata_write(gamedata)
            winner_team = "Paper"
        if scoreboards.index(winner) == 2:
            gamedata['game-played'] += 1
            gamedata['scissor-win'] += 1
            gamedata_write(gamedata)
            winner_team = "Scissor"
        current_status = winner["text"]
        text, previous_score = current_status.split(":")
        final_text = text + ":" + "Winner!"
        winner["text"] = final_text
        game_over()

restart_button = None
statistic_button = None
time_game = 0

def game_over():
    global GAMING, restart_button, time_game, statistic_button
    time_end = time.time()
    time_game = time_end-time_start
    time.sleep(1)
    GAMING = False
    rocks.clear()
    papers.clear()
    scissors.clear()
    canvas.delete('all')
    restart_button = Button(tk, text='Restart', command=restart_game)
    restart_button.place(relx=0.5, rely=0.5, anchor=CENTER)
    statistic_button = Button(tk, text='Statistic', command=statistic)
    statistic_button.place(relx=0.5, rely=0.54, anchor=CENTER) 
    
def statistic():
    time_list = []
    a = 0
    time_increment = time_game / len(rock_number)
    for i in range(len(rock_number)):
        a += time_increment
        time_list.append(a)
    labels = ['Rock', 'Paper', 'Scissor']
    plt.figure()
    plt.stackplot(time_list, rock_number, paper_number, scissor_number, baseline='zero', labels=labels, colors=['red','green','blue'])
    plt.ylim(0, 60)
    plt.title("Rock vs Paper vs Scissor({0} Wins)\nRed:Rock, Green:Paper, Blue:Scissor".format(winner_team))
    plt.xlabel("Time(s)")
    plt.ylabel("Survival Number")
    plt.legend(loc="upper left")
    plt.show()

def restart_game():
    global rocks, papers, scissors, GAMING, restart_button, statistic_button, rock_number, paper_number, scissor_number, time_start
    time_start = time.time()
    try:
        restart_button.destroy()
        statistic_button.destroy()
    except:
        pass
    rock_number = []
    paper_number = []
    scissor_number = []
    rocks = [Rock(canvas, random.randint(50,canvas.winfo_reqwidth()-50), random.randint(50, canvas.winfo_reqheight()-50), round(random.uniform(0.5, 4), 2), round(random.uniform(-4, 4), 2), round(random.uniform(-4, 4), 2)) for i in range(20)]
    papers = [Paper(canvas, random.randint(50,canvas.winfo_reqwidth()-50), random.randint(50, canvas.winfo_reqheight()-50), round(random.uniform(0.5, 4), 2), round(random.uniform(-4, 4), 2), round(random.uniform(-4, 4), 2)) for i in range(20)]
    scissors = [Scissor(canvas, random.randint(50,canvas.winfo_reqwidth()-50), random.randint(50, canvas.winfo_reqheight()-50), round(random.uniform(0.5, 4), 2), round(random.uniform(-4, 4), 2), round(random.uniform(-4, 4), 2)) for i in range(20)]
    GAMING = True

restart_image = os.path.join(base_dir, './restart.png')
restart_image = PhotoImage(file=restart_image)
force_restart_button = Button(tk, text="Restart", image=restart_image, command=restart_game)
force_restart_button.place(x=0, y=60)

def settings():
    global rocks, papers, scissors, restart_button, statistic_button, GAMING, settings_button
    settings_button.config(state="disabled")
    rocks.clear()
    papers.clear()
    scissors.clear()
    try:
        restart_button.destroy()
        statistic_button.destroy()
    except:
        pass
    canvas.delete('all')
    current_gamedata = gamedata_read()
    settings_window = Toplevel(tk)
    settings_window.title("Gaming History")
    settings_window.protocol("WM_DELETE_WINDOW", lambda:[settings_button.config(state="normal"), settings_window.destroy()])
    label = Label(settings_window, text="This is your 'Rock vs Paper vs Scissor' Gaming History.")
    label.pack()
    label1 = Label(settings_window, text='Games Played: {0}'.format(current_gamedata["game-played"]))
    label1.pack()
    if current_gamedata["game-played"] != 0:
        label2 = Label(settings_window, text="Times of Rock won: {0}({1}%)".format(current_gamedata["rock-win"], current_gamedata["rock-win"]/current_gamedata["game-played"]*100))
        label2.pack()
        label3 = Label(settings_window, text="Times of Paper won: {0}({1}%)".format(current_gamedata["paper-win"], current_gamedata["paper-win"]/current_gamedata["game-played"]*100))
        label3.pack()
        label4 = Label(settings_window, text="Times of Scissor won: {0}({1}%)".format(current_gamedata["scissor-win"], current_gamedata["scissor-win"]/current_gamedata["game-played"]*100))
        label4.pack()
    if current_gamedata["game-played"] == 0:
        label2 = Label(settings_window, text="Times of Rock won: 0")
        label2.pack()
        label3 = Label(settings_window, text="Times of Paper won: 0")
        label3.pack()
        label4 = Label(settings_window, text="Times of Scissor won: 0")
        label4.pack()
    delete_data_button = Button(settings_window, text="Delete your game data", command=gamedata_delete)
    delete_data_button.pack()

settings_image = os.path.join(base_dir, './settings.png')
settings_image = PhotoImage(file=settings_image)
settings_button = Button(tk, text="Settings", image=settings_image, command=settings)
settings_button.place(rely=1.0, relx=0, x=0, y=0, anchor=SW)

# For the statistic
rock_number = []
paper_number = []
scissor_number = []

# Mainloop
while True:
    if GAMING == True:
        for rock in rocks:
            rock.draw()    
            rock.fight()
        for paper in papers:
            paper.draw()
            paper.fight()
        for scissor in scissors:
            scissor.draw()
            scissor.fight()
        # Update Scoreboards
        rock_number.append(len(rocks))
        paper_number.append(len(papers))
        scissor_number.append(len(scissors))
        update_scoreboard(len(rocks), len(papers), len(scissors))
    tk.update_idletasks()
    tk.update()