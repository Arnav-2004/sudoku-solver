import time
import pyautogui as pg

grid = []

for _ in range(0, 9):
    row = list(input("Row: "))
    grid.append([int(num) for num in row])

time.sleep(3)

def possible(grid, row, col, num):
    for i in range(0, 9):
        if grid[row][i] == num:
            return False
    for i in range(0, 9):
        if grid[i][col] == num:
            return False
    x0 = (row // 3) * 3
    y0 = (col // 3) * 3
    for i in range(0, 3):
        for j in range(0, 3):
            if grid[x0 + i][y0 + j] == num:
                return False
    return True

def solve(grid):
    for row in range(0, 9):
        for col in range(0, 9):
            if grid[row][col] == 0:
                for num in range(1, 10):
                    if possible(grid, row, col, num):
                        grid[row][col] = num
                        solve(grid)
                        grid[row][col] = 0
                return
    final_grid = []
    for row in grid:
        for num in row:
            final_grid.append(str(num))
    count = 0
    for num in final_grid:
        pg.press(num)
        pg.hotkey("right")
        count += 1
        if count % 9 == 0:
            pg.hotkey("down")
            for _ in range(0, 8):
                pg.hotkey("left")

solve(grid)