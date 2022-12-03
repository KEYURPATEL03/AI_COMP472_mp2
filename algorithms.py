import time
import secondaryMethods as secondary
from childrens import *
from inputPuzzle import *


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

def hUcs(node):
    return len(node["solutionPath"])


def createSolFile(result, initialConfigString, algorithmType, puzzleNumber, fuelLevels):
    solFile = open("./output/"+algorithmType + "sol-" + str(puzzleNumber) + ".txt", "w")
    if result["result"] == "goal_reached":
        solFile.write("Initial board configuration: " + initialConfigString + "\n\n")

        splitted_line = initialConfigString.split(" ")
        puzzle_string = splitted_line[0]
        count = 0
        for i in range(len(puzzle_string)):
            solFile.write(puzzle_string[i] + " ")
            count += 1
            if count == 6:
                solFile.write("\n")
                count = 0
        solFile.write("\n")

        solFile.write("Car fuel available: ")
        fuelsString = ""
        for key in fuelLevels:
            fuelsString += key + ":" + str(fuelLevels[key]) + ", "
        solFile.write(fuelsString[0: len(fuelsString) - 2] + "\n\n")

        runtimeVal = float("{:.2f}".format(result["runtime"]))

        solFile.write("Runtime: " + str(runtimeVal) + " seconds\n")

        solFile.write("Search path length: " + str(result["length_search_path"]) + "\n")

        solFile.write("Solution path length: " + str(len(result["state"]["solutionPath"])) + "\n")

        solFile.write("Solution path: ")
        solPathString = ""
        for path in result["state"]["solutionPath"]:
            solPathString += path["carType"] + " " + path["direction"] + " 1; "
        solFile.write(solPathString[0: len(solPathString) - 2])
        solFile.write("\n\n")

        for path in result["state"]["solutionPath"]:
            pathString = ""
            pathString += path["carType"] + " " + path["direction"] + " 1       "
            pathString += str(path["fuelLevels"][path["carType"]]) + " "
            for puzzleRow in path["puzzle"]:
                for puzzleElem in puzzleRow:
                    pathString += puzzleElem
            solFile.write(pathString + "\n")
        solFile.write("\n")

        finalPuzzle = result["state"]["puzzle"]
        for puzzleRow in finalPuzzle:
            rowString = ""
            for puzzleElem in puzzleRow:
                rowString += puzzleElem + " "
            solFile.write(rowString + "\n")

    else:
        solFile.write("Initial board configuration: " + initialConfigString + "\n\n")

        splitted_line = initialConfigString.split(" ")
        puzzle_string = splitted_line[0]
        count = 0
        for i in range(len(puzzle_string)):
            solFile.write(puzzle_string[i] + " ")
            count += 1
            if count == 6:
                solFile.write("\n")
                count = 0
        solFile.write("\n")

        solFile.write("Car fuel available: ")
        fuelsString = ""
        for key in fuelLevels:
            fuelsString += key + ":" + str(fuelLevels[key]) + ", "
        solFile.write(fuelsString[0: len(fuelsString) - 2] + "\n\n")

        solFile.write("Sorry, could not solve the puzzle as specified.\n")

        solFile.write("Erorr: no solution found.\n\n")

        runtimeVal = float("{:.2f}".format(result["runtime"]))
        solFile.write("Runtime: " + str(runtimeVal) + " seconds")

    solFile.close()


def createSearchFile(result, initialConfigString, algorithmType, puzzleNumber):
    searchFile = open("./output/"+algorithmType+"search-"+str(puzzleNumber)+".txt", "w")
    close_list = result["close_list"]
    for node in close_list:
        nodeString = ""
        if algorithmType.__contains__("ucs"):
            nodeString += "0 "
            nodeString += str(node["Fn"]) + " 0 "
        elif algorithmType.__contains__("gbfs"):
            # h(n)
            nodeString += "0 0 " + str(node["Fn"])+" "
        else:
            #f(n) g(n) h(n)
            hOfN = node["Fn"] - len(node["solutionPath"])
            nodeString += str(node["Fn"]) + " " + str(len(node["solutionPath"])) + " " + str(hOfN) + " "

        for puzzleRow in node["puzzle"]:
            for puzzleElem in puzzleRow:
                nodeString += puzzleElem
        nodeString += " "

        for key in node["fuelLevels"]:
            if node["fuelLevels"][key] != 100:
                nodeString += key + str(node["fuelLevels"][key]) + " "

        searchFile.write(nodeString+"\n")

    searchFile.close()

def solvePuzzle(puzzle, fuels, initialStringConfig, puzzleNumber):  # main function; call algorithm function for all puzzles
    print("Solving puzzle #" + str(puzzleNumber) + "\n")

    # UCS
    print("Using UCS")
    resultUCS = algorithms(puzzle, fuels, hUcs, "ucs")
    createSolFile(resultUCS, initialStringConfig, "ucs-", puzzleNumber, fuels)
    createSearchFile(resultUCS, initialStringConfig, "ucs-", puzzleNumber)
    print("\n")

puzzleList = readpuzzle("sample-input.txt")
for puzzleElem in puzzleList:
    solvePuzzle(puzzleElem["puzzle"], puzzleElem["fuel"], puzzleElem["stringOfPuzzle"], puzzleElem["puzzleNum"])
