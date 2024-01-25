# Rock vs Paper vs Scissor
This is a game which simulates the Rock vs Paper vs Scissor. But we don't really play it(We don't randomly choose:joy:).    
Instead, we put rocks, papers, scissors on the canvas and let them fight with each other. Unfortunately, I am not good at AI technology so actually they just randomly move in straight line, and bounce if they hit the wall. When they "fight"(it means one touches another), for example, if a rock meets a paper, the rock dies, but paper are still alive, and a new paper will be born. Very simple, right?  
This game is written by Python using tkinter, matplotlib modules. Notice that the following tutorial is for BETA2.2!

## Tutorial
### Basic
When you run the py file, a tkinter window should be shown on your screen. If not or error happens, please check if you have correctly installed matplotlib & Pillow. There should be 45 objects running on the canvas, a few buttons and 3 scoreboards. If these run properly, congratulations, you succeed!  
When a team is extinct, they "game over". If two teams "game over", the third will win the game. Only one team is the winner. Now you can press "Restart" button to start another new game.  

### Statistics
When a game ends, you will notice that there are another button to choose: "Statistic" button. If you press it, a new matplotlib window will be created. You can see the comparison of the numbers of the 3 teams in different time of the whole game. Red represents rock, green represents paper, and blue represents scissor. Very intuitive and useful, right?:smile:  
Sometimes you may see this strange game: Scissors are going extinct, but papers eat all the rocks, finally scissors eat all the papers and win. What an interesting game!  





    