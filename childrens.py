import copy
from secondaryMethods import *

def findNextMoves(solutionpath, puzzle, k, start_car, end_car, fuels, heuristic, car_align):
    global car_type
    new_nodes = []
    car_length = end_car - start_car + 1
    if car_align == "horizontal":
        car_type = puzzle[k][start_car]
    elif car_align == "vertical":
        car_type = puzzle[start_car][k]

    for position in reversed(range(start_car)):
        if car_align == "horizontal":
            if puzzle[k][position] != ".":   # move car left
                break
        elif car_align == "vertical":
            if puzzle[position][k] != ".":      # move car up
                break

        new_puzzle = copy.deepcopy(puzzle)  # 6*6 list
        new_fuels = copy.deepcopy(fuels)  # dict
        new_solutionpath = copy.deepcopy(solutionpath)  # list

        displacement = start_car - position  # always move by 1 at a time

        if displacement <= fuels[car_type]:  # to check the car has enough fuel to move
            new_fuels[car_type] = new_fuels[car_type] - displacement  # decrease the fuel level, by amount the car moved
            carPartsToMove = car_length

            for newIndex in range(position,
                                  end_car + 1):  # moving the car, by sending each element left at a time and then

                if carPartsToMove > 0:
                    if car_align == "horizontal":
                        new_puzzle[k][newIndex] = car_type
                    elif car_align == "vertical":
                        new_puzzle[newIndex][k] = car_type
                    carPartsToMove -= 1
                else:
                    if car_align == "horizontal":
                        new_puzzle[k][newIndex] = "."
                    elif car_align == "vertical":
                        new_puzzle[newIndex][k] = "."
                # end of loop
            new_puzzle = valetService(new_puzzle)
            new_solutionpath.append({
                "carType": car_type,
                "direction": "right",  #
                "fuelLevels": new_fuels,
                "puzzle": new_puzzle
            })

            new_node = {
                "puzzle": new_puzzle,
                "solutionPath": new_solutionpath,
                "fuelLevels": new_fuels,
                "stringConfig": stringConfigPuzzle(new_puzzle),
            }

            new_node["fOfN"] = heuristic(new_node)
            new_nodes.append(new_node)

        else:  # this will be executed if car has no fuel
            break
    # end of loop

    for position in range(end_car+1,6):
        if car_align == "horizontal":
            if puzzle[k][position] != ".":
                break
        elif car_align == "vertical":
            if puzzle[position][k] != ".":
                break

        new_puzzle = copy.deepcopy(puzzle)  # 6*6 list
        new_fuels = copy.deepcopy(fuels)  # dict
        new_solutionpath = copy.deepcopy(solutionpath)  # list

        displacement = position - end_car  # always move by 1 at a time

        if displacement <= fuels[car_type]:  # to check the car has enough fuel to move
            new_fuels[car_type] = new_fuels[car_type] - displacement  # decrease the fuel level, by amount the car moved
            carPartsToMove = car_length

            for newIndex in reversed(range(start_car, position + 1)):  # moving the car, by sending each element left at a time and then

                if carPartsToMove > 0:
                    if car_align == "horizontal":
                        new_puzzle[k][newIndex] = car_type
                    elif car_align == "vertical":
                        new_puzzle[newIndex][k] = car_type
                    carPartsToMove -= 1
                else:
                    if car_align == "horizontal":
                        new_puzzle[k][newIndex] = "."
                    elif car_align == "vertical":
                        new_puzzle[newIndex][k] = "."
                # end of loop
            new_puzzle = valetService(new_puzzle)
            new_solutionpath.append({
                "carType": car_type,
                "direction": "right",  #
                "fuelLevels": new_fuels,
                "puzzle": new_puzzle
            })

            new_node = {
                "puzzle": new_puzzle,
                "solutionPath": new_solutionpath,
                "fuelLevels": new_fuels,
                "stringConfig": stringConfigPuzzle(new_puzzle),
            }

            new_node["fOfN"] = heuristic(new_node)
            new_nodes.append(new_node)

        else:  # this will be executed if car has no fuel
            break
    return new_nodes
    # end of loop

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
