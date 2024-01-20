# Import modules
from tkinter import *
import random
import time

GAMING = True

# Initialize Game
class Game:
    def __init__(self):
        tk = Tk()
        self.tk = tk
        self.canvas = Canvas(tk, width=1200, height=850, background='grey')
        self.canvas.pack()

# Initialize three 'competitors'
class Rock:
    def __init__(self, canvas, x, y):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.pos = [self.x, self.y]
        self.images = PhotoImage(file='images/rock.png') # Image size 55px*55px
        self.image = self.canvas.create_image(self.x, self.y, anchor='nw', image=self.images)
        # Get random speed
        self.speed = random.uniform(0.5, 4)
        self.x = random.uniform(-4, 4)
        self.y = random.uniform(-4, 4)
        
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
                papers.append(Paper(game.canvas, self.pos[0], self.pos[1]))
                rocks.remove(self) # Die
                del(self)
                return 0

class Paper:
    def __init__(self, canvas, x, y):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.pos = [self.x, self.y]
        self.images = PhotoImage(file='images/paper.png')
        self.image = self.canvas.create_image(self.x, self.y, anchor='nw', image=self.images)
        self.speed = random.uniform(0.5, 4)
        self.x = random.uniform(-4, 4)
        self.y = random.uniform(-4, 4)

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
                    scissors.append(Scissor(game.canvas, self.pos[0], self.pos[1]))
                    papers.remove(self)
                    del(self)
                    return 0

class Scissor:
    def __init__(self, canvas, x, y):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.pos = [self.x, self.y]
        self.images = PhotoImage(file='images/scissor.png')
        self.image = self.canvas.create_image(self.x, self.y, anchor='nw', image=self.images)
        self.speed = random.uniform(0.5, 4)
        self.x = random.uniform(-4, 4)
        self.y = random.uniform(-4, 4)

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
                    rocks.append(Rock(game.canvas, self.pos[0], self.pos[1]))
                    scissors.remove(self)
                    del(self)
                    return 0

game = Game()
tk = game.tk

canvas = game.canvas
rocks = [Rock(canvas, random.randint(50,canvas.winfo_reqwidth()-50), random.randint(50, canvas.winfo_reqheight()-50)) for i in range(20)]
papers = [Paper(canvas, random.randint(50,canvas.winfo_reqwidth()-50), random.randint(50, canvas.winfo_reqheight()-50)) for i in range(20)]
scissors = [Scissor(canvas, random.randint(50,canvas.winfo_reqwidth()-50), random.randint(50, canvas.winfo_reqheight()-50)) for i in range(20)]

rocks_scoreboard = Label(tk, text="Rock:20")
rocks_scoreboard.place(x=0, y=0)
papers_scoreboard = Label(tk, text="Paper:20")
papers_scoreboard.place(x=0, y=20)
scissors_scoreboard = Label(tk, text="Scissor:20")
scissors_scoreboard.place(x=0, y=40)

def update_scoreboard(rocks_score:int, papers_score:int, scissors_score:int):
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
        current_status = winner["text"]
        text, previous_score = current_status.split(":")
        final_text = text + ":" + "Winner!"
        winner["text"] = final_text
        game_over()

restart_button = None

def game_over():
    time.sleep(2)
    global GAMING, restart_button
    GAMING = False
    rocks.clear()
    papers.clear()
    scissors.clear()
    canvas.delete('all')
    restart_button = Button(tk, text='Restart', command=restart_game)
    restart_button.place(relx=0.5, rely=0.5, anchor=CENTER)

def restart_game():
    global rocks, papers, scissors, GAMING, restart_button
    restart_button.destroy()
    rocks = [Rock(canvas, random.randint(50,canvas.winfo_reqwidth()-50), random.randint(50, canvas.winfo_reqheight()-50)) for i in range(20)]
    papers = [Paper(canvas, random.randint(50,canvas.winfo_reqwidth()-50), random.randint(50, canvas.winfo_reqheight()-50)) for i in range(20)]
    scissors = [Scissor(canvas, random.randint(50,canvas.winfo_reqwidth()-50), random.randint(50, canvas.winfo_reqheight()-50)) for i in range(20)]
    GAMING = True
    
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
        update_scoreboard(len(rocks), len(papers), len(scissors))
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)