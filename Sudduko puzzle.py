import pygame
import sys
import tkinter as tk
from tkinter import ttk
from time import time
import random
from collections import deque

# Sudoku boards
easy_boards = [
    [[5, 3, 0, 0, 7, 0, 0, 0, 0],
     [6, 0, 0, 1, 9, 5, 0, 0, 0],
     [0, 9, 8, 0, 0, 0, 0, 6, 0],
     [8, 0, 0, 0, 6, 0, 0, 0, 3],
     [4, 0, 0, 8, 0, 3, 0, 0, 1],
     [7, 0, 0, 0, 2, 0, 0, 0, 6],
     [0, 6, 0, 0, 0, 0, 2, 8, 0],
     [0, 0, 0, 4, 1, 9, 0, 0, 5],
     [0, 0, 0, 0, 8, 0, 0, 7, 9]],
    # Add more easy boards if needed
]

medium_boards = [
    [[0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0]],
    # Add more medium boards if needed
]

hard_boards = [
    [[0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0]],
    # Add more hard boards if needed
]

# Initialize Pygame
pygame.init()

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (200, 200, 200)
BLUE = (0, 0, 255)

# Screen dimensions
WIDTH, HEIGHT = 540, 600
CELL_SIZE = WIDTH // 9

# Fonts
FONT_SIZE = 40
font = pygame.font.Font(None, FONT_SIZE)

def draw_grid():
    for i in range(10):
        if i % 3 == 0:
            thickness = 4
        else:
            thickness = 1
        pygame.draw.line(screen, BLACK, (i * CELL_SIZE, 0), (i * CELL_SIZE, HEIGHT), thickness)
        pygame.draw.line(screen, BLACK, (0, i * CELL_SIZE), (WIDTH, i * CELL_SIZE), thickness)

def draw_numbers(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] != 0:
                num_text = font.render(str(board[i][j]), True, BLACK)
                screen.blit(num_text, (j * CELL_SIZE + 20, i * CELL_SIZE + 10))

def is_valid(board, num, row, col):
    # Check row and column
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False

    # Check 3x3 square
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[i + start_row][j + start_col] == num:
                return False

    return True

def solve_sudoku_backtracking(board):
    empty_cell = find_empty_cell(board)
    if not empty_cell:
        return True  # Puzzle solved
    else:
        row, col = empty_cell

    for num in range(1, 10):
        if is_valid(board, num, row, col):
            board[row][col] = num

            if solve_sudoku_backtracking(board):
                return True

            board[row][col] = 0  # Backtrack if the current number doesn't lead to a solution

    return False

def find_empty_cell(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return (i, j)
    return None

def revise(board, i, j, X, Y):
    revised = False
    for x in X:
        for y in Y:
            if x != i and y != j and len(board[x][y]) == 1 and board[x][y][0] in board[i][j]:
                board[i][j].remove(board[x][y][0])
                revised = True
    return revised

def AC3(board):
    queue = deque([])
    for i in range(9):
        for j in range(9):
            if len(board[i][j]) > 1:
                queue.append((i, j))

    while queue:
        i, j = queue.popleft()
        if revise(board, i, j, range(9), range(9)):
            if len(board[i][j]) == 0:
                return False
            peers = [(i, y) for y in range(9)] + [(x, j) for x in range(9)] + \
                    [(x, y) for x in range((i // 3) * 3, (i // 3 + 1) * 3)
                     for y in range((j // 3) * 3, (j // 3 + 1) * 3)]
            for p in peers:
                if len(board[p[0]][p[1]]) > 1 and p != (i, j):
                    queue.append(p)
    return True

def solve_sudoku_ac3(board):
    if not AC3(board):
        return False
    return solve_sudoku_backtracking(board)

def solve():
    global selected_difficulty, selected_algorithm, selected_puzzle, time_taken

    difficulty = selected_difficulty.get()
    algorithm = selected_algorithm.get()

    if difficulty == "Easy":
        puzzle = random.choice(easy_boards)
    elif difficulty == "Medium":
        puzzle = random.choice(medium_boards)
    elif difficulty == "Hard":
        puzzle = random.choice(hard_boards)

    start_time = time()
    if algorithm == "Backtracking":
        solve_sudoku_backtracking(puzzle)
    elif algorithm == "AC-3":
        solve_sudoku_ac3(puzzle)
    end_time = time()

    screen.fill(WHITE)
    draw_grid()
    draw_numbers(puzzle)
    pygame.display.update()

    time_taken.set(f"Time taken: {end_time - start_time:.4f} seconds")

def main():
    global screen, selected_difficulty, selected_algorithm, time_taken
    # Create the screen
    screen = pygame.display.set_mode((WIDTH, HEIGHT - 57))  # Adjusted height to eliminate the extra line
    pygame.display.set_caption("Sudoku")

    root = tk.Tk()
    root.title("Sudoku Solver")

    # Tkinter variables
    selected_difficulty = tk.StringVar()
    selected_algorithm = tk.StringVar()
    time_taken = tk.StringVar()
    time_taken.set("Time taken: N/A")

    # Create GUI widgets
    difficulty_label = tk.Label(root, text="Select Difficulty:")
    difficulty_label.pack()
    difficulty_combo = ttk.Combobox(root, textvariable=selected_difficulty, values=["Easy", "Medium", "Hard"])
    difficulty_combo.pack()

    algorithm_label = tk.Label(root, text="Select Algorithm:")
    algorithm_label.pack()
    algorithm_combo = ttk.Combobox(root, textvariable=selected_algorithm, values=["Backtracking", "AC-3"])
    algorithm_combo.pack()

    solve_button = tk.Button(root, text="Solve", command=solve)
    solve_button.pack()

    time_label = tk.Label(root, textvariable=time_taken)
    time_label.pack()

    root.mainloop()

if __name__ == "__main__":
    main()
