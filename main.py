# This is Rock vs Paper vs Scissor source code
# Please read readme.md to learn how to play the game
# My email address: fanfansmilkyway@gmail.com / fanfansmilkyway@qq.com
# Github repository: https://github.com/fanfansmilkyway/Rock-vs-Paper-vs-Scissor

# Import modules(built-in)
from tkinter import * # For GUI
import tkinter.messagebox # For warning messages
import tkinter.filedialog # For choosing files
import shutil # For downloading picture from local
import pickle # For saving gaming data(.dat)
import random
import time # For sleep
import os

# Not built-in(Need to install)
import matplotlib.pyplot as plt # For Statistics
# For pictures resizing and processing(add border)
from PIL import Image as PImage # PImage for avoiding tkinter.Image module
from PIL import ImageOps, ImageTk

# Creating a folder for costomized images
try:
    os.mkdir('costom_image') # Error if folder exists
except:
    pass

gamedata = {}
player = None

# Three useful functions for gamedata processing
def gamedata_read():
    global gamedata
    load_file = open('gamedata.dat', 'rb') # 'rb' means binary read
    gamedata = pickle.load(load_file)
    load_file.close()
    return gamedata

def gamedata_write():
    save_file = open('gamedata.dat', 'wb') # 'wb' means binary write
    pickle.dump(gamedata, save_file)
    save_file.close()

def gamedata_delete():
    if tkinter.messagebox.askokcancel("Delete Anyway", "If you do this, your game data will be deleted forever. You can not undo this. Are you sure you want to delete it?"):
        save_file = open('gamedata.dat', 'wb')
        # Set all to 0 = Delete
        gamedata = {
            'game-played': 0,
            'rock-win': 0,
            'paper-win': 0,
            'scissor-win': 0,
            'play-time': 0,
            'speed': 4
        }
        pickle.dump(gamedata, save_file)
        save_file.close()
    else:
        return 

if os.path.exists('gamedata.dat'):
    gamedata_read()

else:
    save_file = open('gamedata.dat', 'wb+') # 'wb+' means binary write and create
    gamedata = {
        'game-played': 0,
        'rock-win': 0,
        'paper-win': 0,
        'scissor-win': 0,
        'play-time': 0,
        'speed': 4
    }
    pickle.dump(gamedata, save_file)
    save_file.close()

def seconds_to_hms(seconds):
    hours, remainder = divmod(seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    return "{0}h {1}m {2}s".format(hours, minutes, seconds)

base_dir = os.path.dirname(__file__)

# Global variable for functions 'communicating' with each other
GAMING = True
USE_DEFAULT_IMAGE = True
USE_DEFAULT_IMAGE_ = True
SPEED = gamedata['speed']

time_start = time.time()

# Initialize Game
class Game:
    def __init__(self):
        tk = Tk()
        self.tk = tk
        self.tk.title("Rock vs Paper vs Scissor(BETA3.1)") # Remember to change this line when every update
        self.canvas = Canvas(tk, width=1200, height=850, background='grey')
        self.canvas.pack()

# Initialize three 'competitors'
class Rock:
    def __init__(self, canvas, x, y, speed, i_x, i_y):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.pos = [self.x, self.y]
        if USE_DEFAULT_IMAGE_ == True:
            file_path = os.path.join(base_dir, './rock.png')
        if USE_DEFAULT_IMAGE_ == False:
            file_path = os.path.join(base_dir, './costom_image/rock.png')
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
                papers.append(Paper(game.canvas, self.pos[0], self.pos[1], round(random.uniform(0.5, SPEED), 2), round(random.uniform(-SPEED, SPEED), 2), round(random.uniform(-SPEED, SPEED), 2)))
                rocks.remove(self) # Die
                del(self)
                return 0

class Paper:
    def __init__(self, canvas, x, y, speed, i_x, i_y):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.pos = [self.x, self.y]
        if USE_DEFAULT_IMAGE_ == True:
            file_path = os.path.join(base_dir, './paper.png')
        if USE_DEFAULT_IMAGE_ == False:
            file_path = os.path.join(base_dir, './costom_image/paper.png')
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
                    scissors.append(Scissor(game.canvas, self.pos[0], self.pos[1], round(random.uniform(0.5, SPEED), 2), round(random.uniform(-SPEED, SPEED), 2), round(random.uniform(-SPEED, SPEED), 2)))
                    papers.remove(self)
                    del(self)
                    return 0

class Scissor:
    def __init__(self, canvas, x, y, speed, i_x, i_y):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.pos = [self.x, self.y]
        if USE_DEFAULT_IMAGE_ == True:
            file_path = os.path.join(base_dir, './scissor.png')
        if USE_DEFAULT_IMAGE_ == False:
            file_path = os.path.join(base_dir, './costom_image/scissor.png')
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
                    rocks.append(Rock(game.canvas, self.pos[0], self.pos[1], round(random.uniform(0.5, SPEED), 2), round(random.uniform(-SPEED, SPEED), 2), round(random.uniform(-SPEED, SPEED), 2)))
                    scissors.remove(self)
                    del(self)
                    return 0

class Player:
    def __init__(self, canvas):
        # Random values, random life
        self.x = random.randint(50, canvas.winfo_reqwidth()-200)
        self.y = random.randint(50, canvas.winfo_reqheight()-200)
        self.pos = [self.x, self.y]
        self.type = random.choice(['Rock','Paper','Scissor'])
        self.canvas = canvas
        if self.type == 'Rock':
            rocks.append(self)
            if USE_DEFAULT_IMAGE_ == False:
                file_path = os.path.join(base_dir, './costom_image/rock.png')
            if USE_DEFAULT_IMAGE_ == True:
                file_path = os.path.join(base_dir, './rock.png')
        if self.type == 'Paper':
            papers.append(self)
            if USE_DEFAULT_IMAGE_ == False:
                file_path = os.path.join(base_dir, './costom_image/paper.png')
            if USE_DEFAULT_IMAGE_ == True:
                file_path = os.path.join(base_dir, './paper.png')
        if self.type == 'Scissor':
            scissors.append(self)
            if USE_DEFAULT_IMAGE_ == False:
                file_path = os.path.join(base_dir, './costom_image/scissor.png')
            if USE_DEFAULT_IMAGE_ == True:
                file_path = os.path.join(base_dir, './scissor.png')
        self.pilimage = PImage.open(file_path)
        self.pilimage = ImageOps.expand(self.pilimage, border=2, fill='red')
        self.images = ImageTk.PhotoImage(self.pilimage)
        self.image = self.canvas.create_image(self.x, self.y, anchor='nw', image=self.images)
        self.canvas.bind_all('<KeyPress-w>', self.up)
        self.canvas.bind_all('<KeyPress-s>', self.down)
        self.canvas.bind_all('<KeyPress-a>', self.left)
        self.canvas.bind_all('<KeyPress-d>', self.right)
        # Note that self.x, self.y are used twice. One for init position, one for moving
        self.x = 0
        self.y = 0

    # TODO: Don't need to check self.type every time...
    def fight(self):
        if self.type == 'Rock':
            papers_pos = []
            for a in papers:
                papers_pos.append(a.pos)
            
            for pos_x, pos_y in papers_pos: # Rock versus Paper = Die
                # Detect if it touches its component
                if self.pos[0] <= pos_x <= self.pos[0]+55 and self.pos[1] <= pos_y <= self.pos[1]+55 \
                or self.pos[0] <= pos_x+55 <= self.pos[0]+55 and self.pos[1] <= pos_y <= self.pos[1]+55 \
                or self.pos[0] <= pos_x <= self.pos[0]+55 and self.pos[1] <= pos_y+55 <= self.pos[1]+55 \
                or self.pos[0] <= pos_x+55 <= self.pos[0]+55 and self.pos[1] <= pos_y+55 <= self.pos[1]+55:
                    papers.append(Paper(self.canvas, self.pos[0], self.pos[1], round(random.uniform(0.5, SPEED), 2), round(random.uniform(-SPEED, SPEED), 2), round(random.uniform(-SPEED, SPEED), 2)))
                    rocks.remove(self) # Die
                    del(self)
                    return 0
        if self.type == 'Paper':
            scissors_pos = []
            for a in scissors:
                scissors_pos.append(a.pos)
            
            for pos_x, pos_y in scissors_pos: # Die
                if self.pos[0] <= pos_x <= self.pos[0]+55 and self.pos[1] <= pos_y <= self.pos[1]+55 \
                    or self.pos[0] <= pos_x+55 <= self.pos[0]+55 and self.pos[1] <= pos_y <= self.pos[1]+55 \
                    or self.pos[0] <= pos_x <= self.pos[0]+55 and self.pos[1] <= pos_y+55 <= self.pos[1]+55 \
                    or self.pos[0] <= pos_x+55 <= self.pos[0]+55 and self.pos[1] <= pos_y+55 <= self.pos[1]+55:
                        scissors.append(Scissor(self.canvas, self.pos[0], self.pos[1], round(random.uniform(0.5, SPEED), 2), round(random.uniform(-SPEED, SPEED), 2), round(random.uniform(-SPEED, SPEED), 2)))
                        papers.remove(self)
                        del(self)
                        return 0
        if self.type == 'Scissor':
            rocks_pos = []
            for a in rocks:
                rocks_pos.append(a.pos)
            
            for pos_x, pos_y in rocks_pos: # Die
                if self.pos[0] <= pos_x <= self.pos[0]+55 and self.pos[1] <= pos_y <= self.pos[1]+55 \
                    or self.pos[0] <= pos_x+55 <= self.pos[0]+55 and self.pos[1] <= pos_y <= self.pos[1]+55 \
                    or self.pos[0] <= pos_x <= self.pos[0]+55 and self.pos[1] <= pos_y+55 <= self.pos[1]+55 \
                    or self.pos[0] <= pos_x+55 <= self.pos[0]+55 and self.pos[1] <= pos_y+55 <= self.pos[1]+55:
                        rocks.append(Rock(self.canvas, self.pos[0], self.pos[1], round(random.uniform(0.5, SPEED), 2), round(random.uniform(-SPEED, SPEED), 2), round(random.uniform(-SPEED, SPEED), 2)))
                        scissors.remove(self)
                        del(self)
                        return 0 

    def draw(self):
        self.canvas.move(self.image, self.x, self.y)
        self.pos = self.canvas.coords(self.image)
        if self.pos[0] <= 0:
            self.x = 0
            self.y = 0
        if self.pos[1] <= 0:
            self.x = 0
            self.y = 0
        if self.pos[0] + 55 >= self.canvas.winfo_reqwidth():
            self.x = 0
            self.y = 0
        if self.pos[1] + 55 >= self.canvas.winfo_reqheight() - 155:
            self.x = 0
            self.y = 0

    def up(self, evt):
        self.x = 0
        self.y = -SPEED

    def down(self, evt):
        self.x = 0
        self.y = SPEED

    def left(self, evt):
        self.y = 0
        self.x = -SPEED

    def right(self, evt):
        self.y = 0
        self.x = SPEED

game = Game()
tk = game.tk

canvas = game.canvas

def controller():
    def detail():
        detail_window = Toplevel(tk)
        detail_window.protocol("WM_DELETE_WINDOW", lambda:[detail_window.destroy(), button2.config(state='normal')])
        detail_window.title("More detailed information")
        _label1 = Label(detail_window, text="Note that this feature is in BETA(developing) stage.\n(Perhaps there are many bugs in it.)")
        _label1.pack()
        _label2 = Label(detail_window, text="When you start a game that you control, your character will be shown on the screen with a red border.")
        _label2.pack()
        _label3 = Label(detail_window, text="Sometimes you are killed immediately when game starts. It's because you are unlucky and your starting position is next to your natural enemy.\n(How short their lives are!:cry:)")
        _label3.pack()
        _label4 = Label(detail_window, text="I know, it's hard to find your character quickly. We will try to improve this.")
        _label4.pack()
        _label5 = Label(detail_window, text="If you die, the game will keep going instead of stopping. And your dead body will 'lie' there(In fact, this is a bug...).")
        _label5.pack()
        _label6 = Label(detail_window, text="Note that if you restart the game by pressing Restart buttons, your character won't appear. The only way to start a game of this mode is to press Controller button.")
        _label6.pack()
        _label7 = Label(detail_window, text="What's more, you can use your costomized image.")
        _label7.pack()
        _label8 = Label(detail_window, text="By the way, if you want to know more about this game, try to visit our gihub website:https://github.com/fanfansmilkyway/Rock-vs-Paper-vs-Scissor")
        _label8.pack()
    controller_button.config(state='disabled')
    window = Toplevel(tk)
    window.protocol("WM_DELETE_WINDOW", lambda:[window.destroy(), controller_button.config(state='normal')])
    window.title("Control one competitor by yourself")
    label1 = Label(window, text="Be bored with watching them fighting on the battlefield? You can join them!")
    label1.pack()
    label2 = Label(window, text="You will be randomly chosen to join rocks or papers or scissors.")
    label2.pack()
    label3 = Label(window, text="Use 'wasd' to move. Run away from your natural enemy, eat your preys!")
    label3.pack()
    label4 = Label(window, text="Press the button to start the game")
    label4.pack()
    button1 = Button(window, text="Start a new game that you controll", command=lambda:restart_game(controller=True))
    button1.pack()
    button2 = Button(window, text="More detailed information", command=detail)
    button2.pack()

controller_image = os.path.join(base_dir, './controller.png')
controller_image = PhotoImage(file=controller_image)
controller_button = Button(tk, image=controller_image, command=controller)
controller_button.place(relx=1.0, rely=1.0, x=0, y=0, anchor=SE)

rocks = [Rock(canvas, random.randint(50,canvas.winfo_reqwidth()-50), random.randint(50, canvas.winfo_reqheight()-50), round(random.uniform(0.5, SPEED), 2), round(random.uniform(0.5, SPEED), 2), round(random.uniform(-SPEED, SPEED), 2)) for i in range(20)]
papers = [Paper(canvas, random.randint(50,canvas.winfo_reqwidth()-50), random.randint(50, canvas.winfo_reqheight()-50), round(random.uniform(0.5, SPEED), 2), round(random.uniform(0.5, SPEED), 2), round(random.uniform(-SPEED, SPEED), 2)) for i in range(20)]
scissors = [Scissor(canvas, random.randint(50,canvas.winfo_reqwidth()-50), random.randint(50, canvas.winfo_reqheight()-50), round(random.uniform(0.5, SPEED), 2), round(random.uniform(-SPEED, SPEED), 2), round(random.uniform(-SPEED, SPEED), 2)) for i in range(20)]

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
    number_losers = scores.count(0)
    losers = [index for index in range(len(scores)) if scores[index]==0]
    if number_losers == 2:
        if losers == [1,2]:
            gamedata['game-played'] += 1
            gamedata['rock-win'] += 1
            gamedata_write()
            winner = rocks_scoreboard
            winner_team = "Rock"
        if losers == [0,2]:
            gamedata['game-played'] += 1
            gamedata['paper-win'] += 1
            gamedata_write()
            winner = papers_scoreboard
            winner_team = "Paper"
        if losers == [0,1]:
            gamedata['game-played'] += 1
            gamedata['scissor-win'] += 1
            gamedata_write()
            winner = scissors_scoreboard
            winner_team = "Scissor"
        current_status = winner["text"]
        text, _ = current_status.split(":")
        final_text = text + ":" + "Winner!"
        winner["text"] = final_text
        game_over()

restart_button = None
statistic_button = None
time_game = 0

def game_over():
    global GAMING, restart_button, time_game, statistic_button, USE_DEFAULT_IMAGE, USE_DEFAULT_IMAGE_
    USE_DEFAULT_IMAGE_ = USE_DEFAULT_IMAGE
    time_end = time.time()
    time_game = time_end-time_start
    gamedata['play-time'] += time_game
    gamedata_write()
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
    plt.ylim(bottom=0)
    plt.title("Rock vs Paper vs Scissor({0} Wins)\nRed:Rock, Green:Paper, Blue:Scissor".format(winner_team))
    plt.xlabel("Time(s)")
    plt.ylabel("Survival Number")
    plt.legend(loc="upper left")
    plt.show()

def restart_game(controller=False):
    global rocks, papers, scissors, GAMING, restart_button, statistic_button, rock_number, paper_number, scissor_number, time_start, USE_DEFAULT_IMAGE_, USE_DEFAULT_IMAGE, player
    USE_DEFAULT_IMAGE_ = USE_DEFAULT_IMAGE
    try:
        restart_button.destroy()
        statistic_button.destroy()
    except:
        pass
    rock_number.clear()
    paper_number.clear()
    scissor_number.clear()
    rocks = [Rock(canvas, random.randint(50,canvas.winfo_reqwidth()-50), random.randint(50, canvas.winfo_reqheight()-50), round(random.uniform(0.5, SPEED), 2), round(random.uniform(-SPEED, SPEED), 2), round(random.uniform(-SPEED, SPEED), 2)) for i in range(20)]
    papers = [Paper(canvas, random.randint(50,canvas.winfo_reqwidth()-50), random.randint(50, canvas.winfo_reqheight()-50), round(random.uniform(0.5, SPEED), 2), round(random.uniform(-SPEED, SPEED), 2), round(random.uniform(-SPEED, SPEED), 2)) for i in range(20)]
    scissors = [Scissor(canvas, random.randint(50,canvas.winfo_reqwidth()-50), random.randint(50, canvas.winfo_reqheight()-50), round(random.uniform(0.5, SPEED), 2), round(random.uniform(-SPEED, SPEED), 2), round(random.uniform(-SPEED, SPEED), 2)) for i in range(20)]
    if player != None:
        canvas.delete(player.image)
    if controller == True:
        player = Player(canvas)
    GAMING = True
    time_start = time.time()

restart_image = os.path.join(base_dir, './restart.png')
restart_image = PhotoImage(file=restart_image)
force_restart_button = Button(tk, text="Restart", image=restart_image, command=restart_game)
force_restart_button.place(x=0, y=60)

def history():
    global GAMING, history_button
    history_button.config(state="disabled")
    current_gamedata = gamedata_read()
    history_window = Toplevel(tk)
    history_window.title("Gaming History")
    history_window.protocol("WM_DELETE_WINDOW", lambda:[history_button.config(state="normal"), history_window.destroy()])
    label = Label(history_window, text="This is your 'Rock vs Paper vs Scissor' Gaming History.")
    label.pack()
    label1 = Label(history_window, text='Games Played: {0}'.format(current_gamedata["game-played"]))
    label1.pack()
    if current_gamedata["game-played"] != 0:
        label2 = Label(history_window, text="Times of Rock won: {0}({1}%)".format(current_gamedata["rock-win"], round(current_gamedata["rock-win"]/current_gamedata["game-played"]*100,2)))
        label2.pack()
        label3 = Label(history_window, text="Times of Paper won: {0}({1}%)".format(current_gamedata["paper-win"], round(current_gamedata["paper-win"]/current_gamedata["game-played"]*100,2)))
        label3.pack()
        label4 = Label(history_window, text="Times of Scissor won: {0}({1}%)".format(current_gamedata["scissor-win"], round(current_gamedata["scissor-win"]/current_gamedata["game-played"]*100,2)))
        label4.pack()
    if current_gamedata["game-played"] == 0:
        label2 = Label(history_window, text="Times of Rock won: 0")
        label2.pack()
        label3 = Label(history_window, text="Times of Paper won: 0")
        label3.pack()
        label4 = Label(history_window, text="Times of Scissor won: 0")
        label4.pack()
    label5 = Label(history_window, text="Play time: {0}".format(seconds_to_hms(round(current_gamedata["play-time"]))))
    label5.pack()
    delete_data_button = Button(history_window, text="Delete your game data", command=gamedata_delete)
    delete_data_button.pack()

def settings():
    global USE_DEFAULT_IMAGE, SPEED
    def rock_change_file():
        rock_filename = tkinter.filedialog.askopenfilename()
        rock_dst_filename = "costom_image/rock.png"
        shutil.copyfile(rock_filename, rock_dst_filename)
        img = PImage.open(rock_dst_filename)
        new_img = img.resize((55,55))
        new_img.save(rock_dst_filename)
    def paper_change_file():
        paper_filename = tkinter.filedialog.askopenfilename()
        paper_dst_filename = "costom_image/paper.png"
        shutil.copyfile(paper_filename, paper_dst_filename)
        img = PImage.open(paper_dst_filename)
        new_img = img.resize((55,55))
        new_img.save(paper_dst_filename)
    def scissor_change_file():
        scissor_filename = tkinter.filedialog.askopenfilename()
        scissor_dst_filename = "costom_image/scissor.png"
        shutil.copyfile(scissor_filename, scissor_dst_filename)
        img = PImage.open(scissor_dst_filename)
        new_img = img.resize((55,55))
        new_img.save(scissor_dst_filename)
    def use_default_image():
        global USE_DEFAULT_IMAGE
        USE_DEFAULT_IMAGE = True
    def use_costom_image():
        global USE_DEFAULT_IMAGE
        if os.path.exists("costom_image/rock.png") and os.path.exists("costom_image/paper.png") and os.path.exists("costom_image/scissor.png"):
            USE_DEFAULT_IMAGE = False
        else:
            mylist = [os.path.exists("costom_image/rock.png"), os.path.exists("costom_image/paper.png"), os.path.exists("costom_image/scissor.png")]
            type_list = ['rock','paper','scissor']
            missing_index = [index for index in range(len(mylist)) if mylist[index]==0]
            missing = ''
            for i in missing_index:
                missing = missing + ', ' + type_list[i]
            tkinter.messagebox.showerror(title='Error', message="You cannot use costomized images now. Because the following images are missing:\n{0}".format(missing))
    def change_speed():
        global SPEED
        SPEED = slider.get()
        gamedata['speed'] = SPEED
        gamedata_write()

    settings_button.config(state="disabled")
    settings_window = Toplevel(tk)
    settings_window.title("Settings")
    settings_window.protocol("WM_DELETE_WINDOW", lambda:[settings_button.config(state="normal"), settings_window.destroy()])
    label1 = Label(settings_window, text="Set costomized 'Rock', 'Paper', 'Scissor' images\n(Images will be resized)")
    label1.pack()
    button1 = Button(settings_window, text="Rock File", command=rock_change_file)
    button1.pack()
    button2 = Button(settings_window, text="Paper File", command=paper_change_file)
    button2.pack()
    button3 = Button(settings_window, text="Scissor File", command=scissor_change_file)
    button3.pack()
    button4 = Button(settings_window, text="Use Default Images", command=use_default_image)
    button4.pack()
    button5 = Button(settings_window, text="Use Costomized Images", command=use_costom_image)
    button5.pack()
    label2_0 = Label(settings_window, text="Preview(Rock, Paper, Scissor)")
    label2_0.pack()
    # Preview
    if USE_DEFAULT_IMAGE == True:
        label2_image = os.path.join(base_dir, 'rock.png')
    if USE_DEFAULT_IMAGE == False:
        label2_image = os.path.join(base_dir, 'costom_image/rock.png')
    label2_image = PhotoImage(file=label2_image) 
    label2 = Label(settings_window, image=label2_image)
    label2.pack()
    label2.image = label2_image

    if USE_DEFAULT_IMAGE == True:
        label3_image = os.path.join(base_dir, 'paper.png')
    if USE_DEFAULT_IMAGE == False:
        label3_image = os.path.join(base_dir, 'costom_image/paper.png')
    label3_image = PhotoImage(file=label3_image) 
    label3 = Label(settings_window, image=label3_image)
    label3.pack()
    label3.image = label3_image

    if USE_DEFAULT_IMAGE == True:
        label4_image = os.path.join(base_dir, 'scissor.png')
    if USE_DEFAULT_IMAGE == False:
        label4_image = os.path.join(base_dir, 'costom_image/scissor.png')
    label4_image = PhotoImage(file=label4_image) 
    label4 = Label(settings_window, image=label4_image)
    label4.pack()
    label4.image = label4_image

    label5 = Label(settings_window, text="\n\n\nSet average speed:")
    label5.pack()
    label6 = Label(settings_window, text="Because we use different computer, \nso sometimes you need to change objects' average speed to prevent them moving too fast.\nOr you want to a faster game\n(Default 4)")
    label6.pack()
    slider = Scale(settings_window, from_=1, to=10, resolution=0.5, orient=HORIZONTAL, length=250)
    slider.set(SPEED)
    slider.pack()
    button6 = Button(settings_window, text="Save and apply", command=change_speed)
    button6.pack()

# Bottom Left corner
bl_frame = Frame(tk)
bl_frame.place(rely=1.0, relx=0, x=0, y=0, anchor=SW)

history_image = os.path.join(base_dir, './history.png')
history_image = PhotoImage(file=history_image)
history_button = Button(tk, text="Gaming History", image=history_image, command=history)
#history_button.place(rely=1.0, relx=0, x=0, y=0, anchor=SW)
history_button.pack(in_=bl_frame, side=BOTTOM)
settings_image = os.path.join(base_dir, './settings.png')
settings_image = PhotoImage(file=settings_image)
settings_button = Button(tk, text="Gaming History", image=settings_image, command=settings)
settings_button.pack(in_=bl_frame, side=BOTTOM)

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
    time.sleep(0.01)