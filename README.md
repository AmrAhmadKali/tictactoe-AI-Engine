# tictactoe-AI-Engine
Tic Tac Toe game on the command line with ability to play against AI
## Background
As building blocks for the game in both Modes(2 player and AI mode) Python functions are used in 4 different Modules with names model, modelai, view, controller representing a MVC architectural design pattern.
The Project uses JSON files to load and save the game state in the data directory. The Project has also tests in the tests folder that can be run using pytest framework.
## Usage
The program first asks the user to choose in which mode to play(But it skips this Step if there
is unfinished play board saved from previous game) then asks the User which Symbol to play
with first (this Step is also skipped in the AI mode for simplicity and the program let the O
plays first), then the game starts and the user gives the coordinates of his move in numbers
from 0 to 2 for both X and Y coordinates. After each entry the move is checked if its valid then
carried out, and after each update the board is checked for possible winners and whether the
board is full, if so the game is terminated. In parallel after each update of board the game is
loaded to the files in data directory.
