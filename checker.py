"""
This file contains the functions that helps in identifying if the puzzle is goal state and can valet service be ran on
it or not. It also has a checker method to check if given two puzzles are equal.
"""


def goalTest(puzzle):  # This function will be called when a node/board is created to check if it is goal.
    if puzzle[2][4] == "A" and puzzle[2][5] == "A":  # This will check if ambulance is on exit position
        return True
    return False


def valetService(puzzle):  # This will run mandatory valet service on every puzzle for free of cost
    if puzzle[2][5] != "A" and puzzle[2][5] != ".":

        i = 4
        while i >= 2:  # This will only run this position 2 of row 2 because we need two places for ambulance
            if puzzle[2][i] == puzzle[2][5]:
                puzzle[2][i] = "."
            else:
                break

            i -= 1

    return puzzle


def arePuzzlesEqual(puzzle1, puzzle2):  #checks if passed puzzles are equal
    for row in range(0, 6):
        for col in range(0, 6):
            if puzzle1[row][col] != puzzle2[row][col]:
                return False

    return True
