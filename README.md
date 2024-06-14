## Sudduko Puzzle (CSP) Problem
 ![sudduko](https://github.com/Ifra-Zaib/Sudduko-Puzzle--CSP--Problem/assets/172352661/1a28235b-e213-4558-b8e3-4b23a9dc7790)
![menue sudduko](https://github.com/Ifra-Zaib/Sudduko-Puzzle--CSP--Problem/assets/172352661/ce1c899a-1cee-4720-a2a8-e2e139af5621)
## Overview
The Sudoku Solver project aims to solve Sudoku puzzles of varying difficulty levels using the AC-3 (Arc Consistency) algorithm and the Backtracking algorithm. This project includes implementations for solving easy, medium, and hard Sudoku puzzles.

## Features
- Sudoku Puzzle Representation: 9x9 grid representation of Sudoku puzzles.
- AC-3 Algorithm: Enforces arc consistency to reduce the search space before applying the backtracking algorithm.
- Backtracking Algorithm: A depth-first search algorithm to find the solution by exploring possible assignments and backtracking when a conflict is found.
- Puzzle Difficulties: Includes easy, medium, and hard Sudoku puzzles with pre-defined boards.
## Contents
- AC-3 Algorithm
- Backtracking Algorithm
## AC-3 Algorithm
The AC-3 algorithm (Arc Consistency Algorithm #3) is used to simplify the problem by enforcing arc consistency. It systematically removes values from the domains of variables that cannot satisfy the constraints with their neighbors, reducing the problem space for the backtracking algorithm.

## Backtracking Algorithm
The backtracking algorithm is a recursive depth-first search algorithm. It attempts to build a solution incrementally by assigning values to variables and backtracking whenever an inconsistency is detected.
