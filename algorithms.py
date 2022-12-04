""""
The algorithms are mostly similar and written and edited from the pseudocode given in slides.
"""

import time
import secondaryMethods as secondary
from child import *
from inputPuzzle import *
from heuristics import *


def algorithms(puzzle, fuels, heuristic, algo):
    start_time = time.time()
    starting_state = {
        # loading initial state list with initial puzzle with fuel levels and initial empty solution path.
        "puzzle": puzzle,  # value of puzzle key is 6*6 list
        "sol_path": [],  #It is a list that contains dictionaries of each solution move
        "fuel_levels": fuels,  # value of fuel_levels is dict.
        "string_configuration": secondary.stringConfigPuzzle(puzzle)  # value is string
    }

    starting_state["Fn"] = heuristic(starting_state)  # adds f(n) value of a puzzle by calling the respective method

    open_list = []
    close_list = []
    open_list.append(starting_state)

    copy_open_list = [starting_state["string_configuration"]]   #This will be used to check if there is a loop and avoid it
    copy_close_list = []                            #This will be used to check if there is a loop and avoid it

    while len(open_list) > 0:      #as long as open list is not empty dont stop
        current_state = open_list.pop(0)
        copy_open_list.remove(current_state["string_configuration"])

        if secondary.goalTest(current_state["puzzle"]):     #If current state is goal state return with its information
            end_time = time.time()
            return {  # If first state is goal state, then return its information.
                "result": "goal_reached",
                "state": current_state,
                "runtime": end_time - start_time,
                "length_search_path": len(close_list),
                "close_list": close_list
            }

        else:                                           #else add it to close list and find its children
            close_list.append(current_state)
            copy_close_list.append(current_state["string_configuration"])

            child_states = childNodes(current_state, heuristic)

            for each_child in child_states:              #For each child check if it is already there in open or close list, to ensure there is no loop.
                if each_child["string_configuration"] in copy_close_list:

                    # -------This is checked only if the algorithm is A/A*-----------
                    if algo == "A":
                        for i in range(len(close_list)):

                            if each_child["string_configuration"] == close_list[i]["string_configuration"]:  #if close list has puzzle same as child
                                if each_child["Fn"] < close_list[i]["Fn"]:          #then compare their f(n)
                                    open_list.append(each_child)              #append child if value is smaller
                                    copy_open_list.append(each_child["string_configuration"])
                                    copy_close_list.remove(each_child["string_configuration"])
                                    close_list.pop(i)

                                break
                # -------------------------------------------------------------------

                else:
                    if each_child["string_configuration"] in copy_open_list:
                        for i in range(len(open_list)):
                            if secondary.checkPuzzlesIfEqual(each_child["puzzle"], open_list[i]["puzzle"]):

                                if each_child["Fn"] < open_list[i]["Fn"]:
                                    open_list[i] = each_child
                                break

                    else:
                        open_list.append(each_child)
                        copy_open_list.append(each_child["string_configuration"])
            # out of loop
            open_list.sort(key=lambda x: x["Fn"], reverse=False)      #sort open list in terms of f(n) after every loop

    # end of while loop

    end_time = time.time()

    return {
        "result": "no_solution",
        "runtime": end_time - start_time,
        "length_search_path": len(close_list),
        "close_list": close_list
    }




