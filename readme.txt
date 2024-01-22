Python to app:
python3 -m PyInstaller --name 'Rock vs Paper vs Scissor' --icon 'rock-paper-scissors.ico' --windowed --add-data='./rock.png:.' --noconfirm --add-data='./paper.png:.' --add-data='./scissor.png:.' --add-data='./restart.png:.' --noconsole main.py
(Better to set virtual environment to reduce the size of app)