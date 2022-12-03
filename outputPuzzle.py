from algorithms import *
from inputPuzzle import *
from heuristics import *


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
            solPathString += path["carType"] + " " + path["direction"] + str(path["displacement"])+ ";"
        solFile.write(solPathString[0: len(solPathString) - 2])
        solFile.write("\n\n")

        for path in result["state"]["solutionPath"]:
            pathString = ""
            pathString += path["carType"] + " " + path["direction"] + " " + str(path["displacement"])+ "     "
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
        else:   # f(n) g(n) h(n)
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


# ----------------------------------------------------------------------------------------------------------------------------


def solvePuzzle(puzzle, fuels, initialStringConfig, puzzleNumber):  # main function; call algorithm function for all puzzles
    print("Solving puzzle #" + str(puzzleNumber) + "\n")

    # UCS
    print("Using UCS")
    resultUCS = algorithms(puzzle, fuels,uniformCostSearch , "ucs")
    createSolFile(resultUCS, initialStringConfig, "ucs-", puzzleNumber, fuels)
    print("\n")


# ----------------------------------------------------------------------------------------------------------------------------
puzzleList = readpuzzle("sample-input.txt")
for puzzleElem in puzzleList:
    solvePuzzle(puzzleElem["puzzle"], puzzleElem["fuel"], puzzleElem["stringOfPuzzle"], puzzleElem["puzzleNum"])
