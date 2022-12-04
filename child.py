""""
This file contains methods to find children of any given puzzle/state/node.
"""


import copy
from secondaryMethods import *


def moves(sol_path, puzzle, k, start_car, end_car, fuels, heuristic, align):
    child_states = []
    car_length = end_car - start_car + 1
    if align == "horizontal":
        car_type = puzzle[k][start_car]
    else:
        car_type = puzzle[start_car][k]

    for index in reversed(range(start_car)):  #to move car left and up we will start from reverse
        if align == "horizontal":
            if puzzle[k][index] != ".":  # move car left
                break
        else:
            if puzzle[index][k] != ".":  # move car up
                break

        new_puzzle = copy.deepcopy(puzzle)  # 6*6 list
        new_fuels = copy.deepcopy(fuels)  # dict
        new_solution_path = copy.deepcopy(sol_path)  # list

        displacement = start_car - index  # always move by 1 at a time

        if displacement <= fuels[car_type]:  # to check the car has enough fuel to move
            new_fuels[car_type] = new_fuels[car_type] - displacement  # decrease the fuel level, by amount the car moved
            total_car_length = car_length   #the total car that should be moved

            for newIndex in range(index, end_car + 1):  # moving the car, by sending each element left at a time

                if align == "horizontal":
                    if total_car_length > 0:
                        new_puzzle[k][newIndex] = car_type
                        total_car_length -= 1
                    else:
                        new_puzzle[k][newIndex] = "."     #setting the previous index to "." after whole car is moved by 1 index

                else:
                    if total_car_length > 0:
                        new_puzzle[newIndex][k] = car_type
                        total_car_length -= 1
                    else:
                        new_puzzle[newIndex][k] = "."    #setting the previous index to "." after whole car is moved by 1 index

            new_puzzle = valetService(new_puzzle)       #check if any car can be moved by valet free of charge

            if align == "horizontal":
                new_solution_path.append({
                    "carType": car_type,
                    "direction": "left ",
                    "fuel_levels": new_fuels,
                    "puzzle": new_puzzle,
                    "displacement": displacement
                })
            else:
                new_solution_path.append({
                    "carType": car_type,
                    "direction": "up   ",
                    "fuel_levels": new_fuels,
                    "puzzle": new_puzzle,
                    "displacement": displacement
                })

            new_state = {
                "puzzle": new_puzzle,
                "sol_path": new_solution_path,
                "fuel_levels": new_fuels,
                "string_configuration": stringConfigPuzzle(new_puzzle),
            }

            new_state["Fn"] = heuristic(new_state)   #calculating the heuristic of the new node
            child_states.append(new_state)

        else:
            break

    for index in range(end_car + 1, 6):
        if align == "horizontal":
            if puzzle[k][index] != ".":  # move car right
                break
        else:
            if puzzle[index][k] != ".":  # move car down
                break

        new_puzzle = copy.deepcopy(puzzle)  # 6*6 list
        new_fuels = copy.deepcopy(fuels)  # dict
        new_solution_path = copy.deepcopy(sol_path)  # list

        displacement = index - end_car  # always move by 1 at a time

        if displacement <= fuels[car_type]:  # to check the car has enough fuel to move
            new_fuels[car_type] = new_fuels[car_type] - displacement  # decrease the fuel level, by amount the car moved
            total_car_length = car_length

            for newIndex in reversed(range(start_car, index + 1)):  # moving the car, by sending each element left at a time and then
                if align == "horizontal":
                    if total_car_length > 0:
                        new_puzzle[k][newIndex] = car_type

                        total_car_length -= 1
                    else:
                        new_puzzle[k][newIndex] = "."  #setting the previous index to "." after whole car is moved by 1 index

                else:
                    if total_car_length > 0:
                        new_puzzle[newIndex][k] = car_type

                        total_car_length -= 1
                    else:
                        new_puzzle[newIndex][k] = "."   #setting the previous index to "." after whole car is moved by 1 index

            new_puzzle = valetService(new_puzzle)

            if align == "horizontal":
                new_solution_path.append({
                    "carType": car_type,
                    "direction": "right",
                    "fuel_levels": new_fuels,
                    "puzzle": new_puzzle,
                    "displacement": displacement
                })
            else:
                new_solution_path.append({
                    "carType": car_type,
                    "direction": "down ",
                    "fuel_levels": new_fuels,
                    "puzzle": new_puzzle,
                    "displacement": displacement
                })

            new_state = {
                "puzzle": new_puzzle,
                "sol_path": new_solution_path,
                "fuel_levels": new_fuels,
                "string_configuration": stringConfigPuzzle(new_puzzle),
            }

            new_state["Fn"] = heuristic(new_state)
            child_states.append(new_state)

        else:
            break

    return child_states

# =================================================================================================================


def childNodes(state, heuristic):
    new_state = copy.deepcopy(state)
    children = []  # child node list
    cars_moved = []
    sol_path = new_state["sol_path"]
    puzzle = new_state["puzzle"]
    fuels = new_state["fuel_levels"]
    align = ""

    for row in range(0, 6):

        for column in range(0, 6):
            if (puzzle[row][column] not in cars_moved) and (puzzle[row][column] != "."):
                cars_moved.append(puzzle[row][column])

                if (column <= 4) and (puzzle[row][column] == puzzle[row][column + 1]):  # horizontal car *
                    finishing_index_horizontal = column  # this will be used to find length of the car
                    for i in range(column, 6):  # The loop will go till index 5 because there are total 6 elements in a row. *
                        if puzzle[row][i] != puzzle[row][column]:  # if simultaneous horizontal elements are not equal then, it is not a car and break.
                            break
                        else:
                            finishing_index_horizontal = i

                        align = "horizontal"
                    horizontal_children = moves(sol_path, puzzle, row, column, finishing_index_horizontal, fuels, heuristic, align)
                    children += horizontal_children

                elif (row <= 4) and (puzzle[row][column] == puzzle[row + 1][column]):  # vertical car *
                    finishing_index_vertical = row  # the starting index of the horizontal car
                    for j in range(row, 6):  # The loop will go till index 5 because there are total 6 rows. *
                        if puzzle[j][column] != puzzle[row][column]:  # if simultaneous horizontal elements are not equal then, it is not a car and break.
                            break
                        else:
                            finishing_index_vertical = j

                        align = "vertical"
                    vertical_children = moves(sol_path, puzzle, column, row, finishing_index_vertical, fuels, heuristic, align)
                    children += vertical_children

    return children