from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.get("https://sudoku.com/")
assert "Sudoku" in driver.title

dificulty_select = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "difficulty-label"))
    )
dificulty_select.click()
t = dificulty_select.find_elements_by_tag_name("li")[3]
t.click()

while True:
    time.sleep(2)
    gameTable = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "game-table"))
        )
    allCells = gameTable.find_elements_by_class_name("game-cell")

    i = 0
    sudokuTable = [[]]
    for x, cell in enumerate(allCells):
        if x % 9 == 0 and x != 0:
            sudokuTable.append([])
            i += 1
        value = cell.find_element_by_class_name("cell-value")
        try:
            text = value.find_element_by_tag_name("svg")
        except:
            sudokuTable[i].append(0)
            continue
        w, h = (text.get_attribute("width"), text.get_attribute("height"))
        w = int(w)
        h = int(h)
        if w == 12:
            sudokuTable[i].append(1)
        elif w == 20:
            if h == 30:
                sudokuTable[i].append(7)
            else:
                sudokuTable[i].append(2)
        elif w == 21:
            if h == 31:
                sudokuTable[i].append(5)
            else:
                sudokuTable[i].append(3)
        elif w == 22:
            s = text.find_element_by_tag_name("path").get_attribute("d")[0:6]
            if s == "M10.96":
                sudokuTable[i].append(6)
            else:
                sudokuTable[i].append(8)
        elif w == 23:
            sudokuTable[i].append(9)
        else:
            sudokuTable[i].append(4)

    def solve(bo):
        find = find_empty(bo)
        if not find:
            return True
        else:
            row, col = find

        for i in range(1, 10):
            if valid(bo, i, (row, col)):
                bo[row][col] = i

                if solve(bo):
                    return True

                bo[row][col] = 0

        return False

    def valid(bo, num, pos):
        for i in range(len(bo[0])):
            if bo[pos[0]][i] == num and pos[1] != i:
                return False

        for i in range(len(bo)):
            if bo[i][pos[1]] == num and pos[0] != i:
                return False

        box_x = pos[1] // 3
        box_y = pos[0] // 3

        for i in range(box_y*3, box_y*3 + 3):
            for j in range(box_x * 3, box_x*3 + 3):
                if bo[i][j] == num and (i, j) != pos:
                    return False

        return True

    def find_empty(bo):
        for i in range(len(bo)):
            for j in range(len(bo[0])):
                if bo[i][j] == 0:
                    return (i, j)

        return None

    backup_table = list(map(list, sudokuTable))
    solve(sudokuTable)

    numpad = driver.find_elements_by_class_name("numpad-item")
    for yp, y in enumerate(backup_table):
        for xp, x in enumerate(y):
            if x == 0:
                allCells[yp*9 + xp].click()
                numpad[sudokuTable[yp][xp] - 1].click()
        if yp == 6:
            driver.execute_script("arguments[0].scrollIntoView();", gameTable)

    play_again = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "button-play"))
        )
    time.sleep(2)
    driver.execute_script("arguments[0].click();", play_again)