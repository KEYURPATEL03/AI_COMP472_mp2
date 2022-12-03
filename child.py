import copy
from secondaryMethods import *


def moves(sol_path, puzzle, k, start_car, end_car, fuels, heuristic, align):
    new_nodes = []
    car_length = end_car - start_car + 1
    if align == "horizontal":
        car_type = puzzle[k][start_car]
    else:
        car_type = puzzle[start_car][k]

    for position in reversed(range(start_car)):
        if align == "horizontal":
            if puzzle[k][position] != ".":  # move car left
                break
        else:
            if puzzle[position][k] != ".":  # move car up
                break

        new_puzzle = copy.deepcopy(puzzle)  # 6*6 list
        new_fuels = copy.deepcopy(fuels)  # dict
        new_solutionpath = copy.deepcopy(sol_path)  # list

        displacement = start_car - position  # always move by 1 at a time

        if displacement <= fuels[car_type]:  # to check the car has enough fuel to move
            new_fuels[car_type] = new_fuels[car_type] - displacement  # decrease the fuel level, by amount the car moved
            carPartsToMove = car_length

            for newIndex in range(position, end_car + 1):  # moving the car, by sending each element left at a time and then

                if align == "horizontal":
                    if carPartsToMove > 0:
                        new_puzzle[k][newIndex] = car_type
                        #  new_puzzle[newIndex][k] = car_type
                        carPartsToMove -= 1
                    else:
                        new_puzzle[k][newIndex] = "."

                else:
                    if carPartsToMove > 0:
                        new_puzzle[newIndex][k] = car_type
                        #  new_puzzle[newIndex][k] = car_type
                        carPartsToMove -= 1
                    else:
                        new_puzzle[newIndex][k] = "."

            new_puzzle = valetService(new_puzzle)

            if align == "horizontal":
                new_solutionpath.append({
                    "carType": car_type,
                    "direction": "left   ",
                    "fuelLevels": new_fuels,
                    "puzzle": new_puzzle
                })
            else:
                new_solutionpath.append({
                    "carType": car_type,
                    "direction": "up   ",
                    "fuelLevels": new_fuels,
                    "puzzle": new_puzzle
                })

            new_node = {
                "puzzle": new_puzzle,
                "solutionPath": new_solutionpath,
                "fuelLevels": new_fuels,
                "stringConfig": stringConfigPuzzle(new_puzzle),
            }

            new_node["Fn"] = heuristic(new_node)
            new_nodes.append(new_node)

        else:
            break

    for position in range(end_car + 1, 6):
        if align == "horizontal":
            if puzzle[k][position] != ".":  # move car left
                break
        else:
            if puzzle[position][k] != ".":  # move car up
                break

        new_puzzle = copy.deepcopy(puzzle)  # 6*6 list
        new_fuels = copy.deepcopy(fuels)  # dict
        new_solutionpath = copy.deepcopy(sol_path)  # list

        displacement = position - end_car  # always move by 1 at a time

        if displacement <= fuels[car_type]:  # to check the car has enough fuel to move
            new_fuels[car_type] = new_fuels[car_type] - displacement  # decrease the fuel level, by amount the car moved
            carPartsToMove = car_length

            for newIndex in reversed(range(start_car, position + 1)):  # moving the car, by sending each element left at a time and then
                if align == "horizontal":
                    if carPartsToMove > 0:
                        new_puzzle[k][newIndex] = car_type

                        carPartsToMove -= 1
                    else:
                        new_puzzle[k][newIndex] = "."

                else:
                    if carPartsToMove > 0:
                        new_puzzle[newIndex][k] = car_type

                        carPartsToMove -= 1
                    else:
                        new_puzzle[newIndex][k] = "."

            new_puzzle = valetService(new_puzzle)

            if align == "horizontal":
                new_solutionpath.append({
                    "carType": car_type,
                    "direction": "right",
                    "fuelLevels": new_fuels,
                    "puzzle": new_puzzle
                })
            else:
                new_solutionpath.append({
                    "carType": car_type,
                    "direction": "down ",
                    "fuelLevels": new_fuels,
                    "puzzle": new_puzzle
                })

            new_node = {
                "puzzle": new_puzzle,
                "solutionPath": new_solutionpath,
                "fuelLevels": new_fuels,
                "stringConfig": stringConfigPuzzle(new_puzzle),
            }

            new_node["Fn"] = heuristic(new_node)
            new_nodes.append(new_node)

        else:
            break

    return new_nodes


def childNodes(state, heuristic):
    new_state = copy.deepcopy(state)
    children = []  # child node list
    cars_moved = []
    sol_path = new_state["solutionPath"]
    puzzle = new_state["puzzle"]
    fuels = new_state["fuelLevels"]
    align = ""

    for row in range(0, 6):

        for column in range(0, 6):
            if (puzzle[row][column] not in cars_moved) and (puzzle[row][column] != "."):
                cars_moved.append(puzzle[row][column])

                if (column +1 != 6) and (puzzle[row][column] == puzzle[row][column + 1]):  # horizontal car *
                    finishing_index_horizontal = column  # this will be used to find length of the car
                    for i in range(column, 6):  # The loop will go till index 5 because there are total 6 elements in a row. *
                        if puzzle[row][i] != puzzle[row][column]:  # if simultaneous horizontal elements are not equal then, it is not a car and break.
                            break
                        else:
                            finishing_index_horizontal = i

                        align = "horizontal"
                    horizontal_children = moves(sol_path, puzzle, row, column, finishing_index_horizontal, fuels, heuristic, align)
                    children += horizontal_children

                elif (row +1 != 6) and (puzzle[row][column] == puzzle[row + 1][column]):  # vertical car *
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