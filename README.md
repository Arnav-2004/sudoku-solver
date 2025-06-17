# Sudoku Solver

This repository contains two implementations of a Sudoku solver:

1. A desktop-based solver that uses PyAutoGUI to input solutions
2. A web-based solver that automates [sudoku.com](https://sudoku.com/) using Selenium

## Implementation 1: Desktop Sudoku Solver

This implementation solves a Sudoku puzzle entered via the command line and automatically inputs the solution using PyAutoGUI.

### Requirements

- Python 3
- PyAutoGUI (`pip install pyautogui`)

### Usage

1. Run the script: `python desktop_solver.py`
2. When prompted, enter each row of the Sudoku puzzle as a continuous string of digits (use 0 for empty cells)
3. After 3 seconds (to allow you to switch to your Sudoku application), the solver will automatically input the solution

### How It Works

- The solver uses a backtracking algorithm to find the solution
- After solving, it uses PyAutoGUI to:
  - Type each number
  - Move right after each entry
  - Move down and back to the left at the end of each row

## Implementation 2: Web Sudoku Solver

This implementation automatically plays Sudoku on [sudoku.com](https://sudoku.com/) using Selenium.

### Requirements

- Python 3
- Selenium (`pip install selenium`)
- ChromeDriver (must match your Chrome version)

### Usage

1. Run the script: `python web_solver.py`
2. The script will:
   - Open Chrome and navigate to sudoku.com
   - Select the "Expert" difficulty level
   - Read the current puzzle
   - Solve it using the backtracking algorithm
   - Input the solution automatically
   - Click "Play Again" when finished

### How It Works

1. The script reads the puzzle by analyzing SVG attributes of the numbers on the page
2. It uses a backtracking algorithm to solve the puzzle
3. It clicks each cell and uses the on-screen numpad to input the solution
4. After completing the puzzle, it automatically starts a new game

## Algorithm Details

Both implementations use a backtracking algorithm with the following key functions:

### `possible()`/`valid()`

Checks if a number can be placed in a given cell by verifying:

- No duplicate in the row
- No duplicate in the column
- No duplicate in the 3x3 subgrid

### `solve()`

The main solving function that:

1. Finds the next empty cell
2. Tries numbers 1-9 in that cell
3. Recursively attempts to solve the puzzle with each valid number
4. Backtracks if a solution isn't found

## Notes

- The desktop version requires you to manually switch to your Sudoku application within 3 seconds
- The web version is specifically designed for sudoku.com and may need adjustments for other Sudoku websites
- For the web version, ensure ChromeDriver is in your PATH or specify its location in the code
