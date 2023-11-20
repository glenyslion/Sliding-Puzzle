# Sliding Puzzle

**CSC1002 Individual Project: Sliding Puzzle**

<a href = "https://github.com/glenyslion/Sliding-Puzzle/blob/main/Sliding%20Puzzle.py"> Sliding Puzzle Code </a>

Design and develop an interactive sliding puzzle game for both 8 and 15 numbers. For an 8-number puzzle, it has a square-framed board consisting of 8 square tiles, numbered 1 to 8, initially placed in random order, while a 15-number puzzle there are 15 numbered square tiles, from 1 to 15, as shown above. The board has an empty space where an adjacent tile can be slid to. The objective of the game is to re-arrange the tiles into a sequential order by their numbers (left to right, top to bottom) by repeatedly making sliding moves (left, right, up or down). The following figure shows an example of an 8-number puzzle where “INITIAL” is the starting point of the game, and the player needs to repeatedly slide an adjacent tile, one at a time, to the currently unoccupied space (the empty space) until all numbers appear sequentially, ordered from left to right, top to bottom, shown as “FINAL”. 

<p align="center">
<img width="406" alt="image" src="https://github.com/glenyslion/Sliding-Puzzle/assets/69634320/1acea633-409a-4a96-86fa-6c9fbbd91476">
</p>

**Instructions:**
1. At the start of the game, display a brief introduction about the game.
2. Prompt user to enter the 4 letters used for the left, right, up and down moves. User is free to pick any four letters such as j, k, r, f for left, right, up and down respectively.
3. Prompt user for selection of either 8 or 15 puzzle, then generate a randomized, **SOLVABLE** 8 or 15-tile puzzle accordingly; have it displayed on the screen using simple ASCII characters.
4. Repeatedly prompt player the sliding direction (left, right, up or down) - the direction that the adjacent tile to be moved (not the empty location). In the prompt the valid sliding move(s) are shown together with the designated letter (from step 2 above). For example: a. Enter your move (left-j, right-k) >
5. After each move, show the updated puzzle on the screen and prompt further direction if needed.
6. Inform user when the puzzle is solved (i.e. the numbered tiles are in sequential order, left to right, top to bottom); then prompt user to continue another game or end the program.
7. Track total number of moves made for each game and have it displayed as the puzzle is solved.

Logic for solvable sliding puzzle: https://www.geeksforgeeks.org/check-instance-15-puzzle-solvable/
