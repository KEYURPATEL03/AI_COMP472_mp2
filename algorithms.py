import time
import secondaryMethods as secondary
from childrens import *


def algorithms(puzzle, fuels, heuristic, algo):
    start_time = time.time()
    starting_state = {
        # loading initial state list with initial puzzle with fuel levels and initial empty solution path.
        "puzzle": puzzle,  # value of puzzle key is 6*6 list
        "solutionPath": [],
        "fuelLevels": fuels,  # value of fuelLevels is dict.
        "stringConfig": secondary.stringConfigPuzzle(puzzle)  # value is string
    }

    starting_state["Fn"] = heuristic(starting_state)  # adds f(n) value of a puzzle by calling the respective method

    open_list = [starting_state]
    close_list = []
    # open_list.append(starting_state)

    copy_open_list = {starting_state["stringConfig"]: 1}
    copy_close_list = {}
    # copy_open_list.append(starting_state["stringConfig"])

    nbsimilar = 0
    nbsimilar2 = 0

    while len(open_list) > 0:
        current_state = open_list.pop(0)
        del copy_open_list[current_state["stringConfig"]]

        if secondary.goalTest(current_state["puzzle"]):
            end_time = time.time()
            return {  # If first state is goal state, then return its information.
                "result": "goal_reached",
                "state": current_state,
                "runtime": end_time - start_time,
                "length_search_path": len(close_list),
                "close_list": close_list
            }

        else:
            close_list.append(current_state)
            copy_close_list[current_state["stringConfig"]] = 1  # *

            child_states = childNodes(current_state, heuristic)

            for each_child in child_states:
                if each_child["stringConfig"] in copy_close_list:
                    nbsimilar = nbsimilar + 1  # if there is loop increment this
                    # -------This is checked only if the algorithm is A/A*-----------
                    if algo == "A":
                        for i in range(len(close_list)):

                            if each_child["stringConfig"] == close_list[i]["stringConfig"]:
                                if each_child["Fn"] < close_list[i]["Fn"]:
                                    open_list.append(each_child)
                                    copy_open_list[each_child["stringConfig"]] = 1
                                    del copy_close_list[each_child["stringConfig"]]
                                    close_list.pop(i)

                                break
                # -------------------------------------------------------------------

                else:
                    if each_child["stringConfig"] in copy_open_list:
                        for i in range(len(open_list)):
                            if secondary.checkPuzzlesIfEqual(each_child["puzzle"], open_list[i]["puzzle"]):
                                nbsimilar2 += 1
                                if each_child["Fn"] < open_list[i]["Fn"]:
                                    open_list[i] = each_child
                                break

                    else:
                        open_list.append(each_child)
                        copy_open_list[each_child["stringConfig"]] = 1
            # out of loop
            open_list.sort(key=lambda x: x["Fn"], reverse=False)

        print("\rLength closedList: " + str(len(close_list)) + "; Length open list: " + str(len(open_list)), end="")
    # end of while loop

    end_time = time.time()

    return {
        "result": "no_solution",
        "runtime": end_time - start_time,
        "length_search_path": len(close_list),
        "close_list": close_list
    }


# =====================================================================================================================
