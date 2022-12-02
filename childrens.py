"""
The methods in this file will return the child nodes/state/puzzle of any given puzzle. It will first find the
alignment of the car, if it is horizontal or vertical and then length of the car and then return, child states.
"""

import copy


def childNodes(puzzle, heuristic):
    children = []
    cars_moved= []
    sol_path = puzzle["solPath"]
    temp_puzzle = puzzle["puzzle"]
    fuel = puzzle["fuels"]

    for row in range(0, 6):

        for column in range(0, 6):
            if (temp_puzzle[row][column] not in cars_moved) and (temp_puzzle[row][column] != "."):
                cars_moved.append(temp_puzzle[row][column])

                if (column <= 4) and (temp_puzzle[row][column] == temp_puzzle[row][column + 1]): #horizontal car
                    finishing_index_horizontal = column   #This will be used to find length of the car
                    for i in range(column + 2, 6):  #The loop will go till index 5 because there are total 6 elements in a row.
                        if puzzle[row][i] != puzzle[row][column]:  # if simultaneous horizontal elements are not equal then, it is not a car and break.
                            break
                        else:
                            finishing_index_horizontal = i

                    car_align = "horizontal"
                    horizontal_children = findNextMoves(sol_path, temp_puzzle, row, column, finishing_index_horizontal, fuel, heuristic, car_align)
                    children += horizontal_children

                elif (row <= 4) and (temp_puzzle[row][column] == temp_puzzle[row + 1][column]): #vertical car
                    finishing_index_vertical = row  # the starting index of the horizontal car
                    for i in range(row + 2, 6):  #The loop will go till index 5 because there are total 6 rows.
                        if puzzle[i][column] != puzzle[row][column]:  # if simultaneous horizontal elements are not equal then, it is not a car and break.
                            break
                        else:
                            finishing_index_vertical = i

                    car_align = "vertical"
                    vertical_children = findNextMoves(sol_path, temp_puzzle, column, row, finishing_index_vertical, fuel, heuristic, car_align)
                    children += vertical_children

    return children


def findNextMoves(sol_path, temp_puzzle, i, j):
    pass

