"""
This file will contain all the heuristic function for calculating f(n). For Uniform cost search f(n) = g(n),
for GBFS f(n) = h(n) and, for A/A* f(n) = g(n) + h(n).
"""


def uniformCostSearch(state):
    return len(state["solutionPath"])


def GBFSh1(state):
    puzzle = state["puzzle"]
    row_with_ambulance = puzzle[2]
    unique_cars = []
    ambulance_starting_index = 0

    for i in range(len(row_with_ambulance)):
        if row_with_ambulance[i] == "A":
            ambulance_starting_index = i
            break

    for i in range(ambulance_starting_index, len(row_with_ambulance)):
        if row_with_ambulance[i] != "A" and row_with_ambulance[i] != ".":
            if row_with_ambulance[i] not in unique_cars:
                unique_cars.append(row_with_ambulance[i])

    return len(unique_cars)


def GBFSh2(state):
    puzzle = state["puzzle"]
    row_with_ambulance = puzzle[2]
    blocked_positions = 0
    ambulance_starting_index = 0

    for i in range(len(row_with_ambulance)):
        if row_with_ambulance[i] == "A":
            ambulance_starting_index = i
            break

    for i in range(ambulance_starting_index, len(row_with_ambulance)):
        if row_with_ambulance[i] != "A" and row_with_ambulance[i] != ".":
            blocked_positions += 1

    return blocked_positions


def GBFSh3(state):
    return 20 * GBFSh1(state)  #noticed that increasing constant value up to certain limit was decreasing solution time


def GBFSh4(state):
    puzzle = state["puzzle"]
    total_cars_length = 0
    for row in range(0, 6):
        for column in range(0, 6):
            if puzzle[row][column] != ".":
                total_cars_length +=1

    return total_cars_length - 2


def Ah1(state):
    return uniformCostSearch(state) + GBFSh1(state)


def Ah2(state):
    return uniformCostSearch(state) + GBFSh2(state)


def Ah3(state):
    return uniformCostSearch(state) + GBFSh3(state)


def Ah4(state):
    return uniformCostSearch(state) + GBFSh4(state)