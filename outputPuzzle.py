from algorithms import *
from inputPuzzle import *
from heuristics import *
import xlsxwriter


def createSolFile(result, initialConfigString, algorithmType, puzzleNumber, fuelLevels):
    solFile = open("./output/solution_files/"+algorithmType + "sol-" + str(puzzleNumber) + ".txt", "w")
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
    searchFile = open("./output/search_files/"+algorithmType+"search-"+str(puzzleNumber)+".txt", "w")
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
    resultUCS = algorithms(puzzle, fuels, uniformCostSearch, "ucs")
    createSolFile(resultUCS, initialStringConfig, "ucs-", puzzleNumber, fuels)
    createSearchFile(resultUCS, initialStringConfig, "ucs-", puzzleNumber)
    print("\n")

    # GBFS heuristic 1
    print("Using GBFS heuristic 1")
    resultGBFS1 = algorithms(puzzle, fuels, GBFSh1, "gbfs")
    createSolFile(resultGBFS1, initialStringConfig, "gbfs-h1-", puzzleNumber, fuels)
    createSearchFile(resultGBFS1, initialStringConfig, "gbfs-h1-", puzzleNumber)
    print("\n")

    # GBFS heuristic 2
    print("Using GBFS heuristic 2")
    resultGBFS2 = algorithms(puzzle, fuels, GBFSh2, "gbfs")
    createSolFile(resultGBFS2, initialStringConfig, "gbfs-h2-", puzzleNumber, fuels)
    createSearchFile(resultGBFS2, initialStringConfig, "gbfs-h2-", puzzleNumber)
    print("\n")

    # GBFS heuristic 3
    print("Using GBFS heuristic 3")
    resultGBFS3 = algorithms(puzzle, fuels, GBFSh3, "gbfs")
    createSolFile(resultGBFS3, initialStringConfig, "gbfs-h3-", puzzleNumber, fuels)
    createSearchFile(resultGBFS3, initialStringConfig, "gbfs-h3-", puzzleNumber)
    print("\n")

    # GBFS heuristic 4
    print("Using GBFS heuristic 4")
    resultGBFS4 = algorithms(puzzle, fuels, GBFSh4, "gbfs")
    createSolFile(resultGBFS4, initialStringConfig, "gbfs-h4-", puzzleNumber, fuels)
    createSearchFile(resultGBFS4, initialStringConfig, "gbfs-h4-", puzzleNumber)
    print("\n")

    # A heuristic 1
    print("Using A heuristic 1")
    resultA1 = algorithms(puzzle, fuels, Ah1, "a")
    createSolFile(resultA1, initialStringConfig, "a-h1-", puzzleNumber, fuels)
    createSearchFile(resultA1, initialStringConfig, "a-h1-", puzzleNumber)
    print("\n")

    # A heuristic 2
    print("Using A heuristic 2")
    resultA2 = algorithms(puzzle, fuels, Ah2, "a")
    createSolFile(resultA2, initialStringConfig, "a-h2-", puzzleNumber, fuels)
    createSearchFile(resultA2, initialStringConfig, "a-h2-", puzzleNumber)
    print("\n")

    # A heuristic 3
    print("Using A heuristic 3")
    resultA3 = algorithms(puzzle, fuels, Ah3, "a")
    createSolFile(resultA3, initialStringConfig, "a-h3-", puzzleNumber, fuels)
    createSearchFile(resultA3, initialStringConfig, "a-h3-", puzzleNumber)
    print("\n")

    # A heuristic 4
    print("Using A heuristic 4")
    resultA4 = algorithms(puzzle, fuels, Ah4, "a")
    createSolFile(resultA4, initialStringConfig, "a-h4-", puzzleNumber, fuels)
    createSearchFile(resultA4, initialStringConfig, "a-h4-", puzzleNumber)
    print("\n")


# ---------------------------------------------------------------------------------------------------------------------
puzzleList = readpuzzle("sample-input.txt")
for puzzleElem in puzzleList:
    solvePuzzle(puzzleElem["puzzle"], puzzleElem["fuel"], puzzleElem["stringOfPuzzle"], puzzleElem["puzzleNum"])


# ------------------------------------------For writing to excel sheet-------------------------------------------------

puzzle50RandomList = readpuzzle("50Puzzles.txt")

workbook = xlsxwriter.Workbook("50PuzzlesOutput.xlsx")
worksheet = workbook.add_worksheet()

worksheet.write(0, 0, "Puzzle Number")
worksheet.write(0, 1, "Algorithm")
worksheet.write(0, 2, "Heuristic")
worksheet.write(0, 3, "Length of the Solution")
worksheet.write(0, 4, "Length of the Search Path")
worksheet.write(0, 5, "Execution Time (in seconds)")

def solvePuzzleInSpreadsheet(puzzle, fuelLevels, puzzleNumber, worksheet):

    print("Solving puzzle #"+str(puzzleNumber)+"\n")

    #UCS
    worksheet.write(((puzzleNumber - 1) * 9)+1, 0, puzzleNumber)
    worksheet.write(((puzzleNumber - 1) * 9)+1, 1, "UCS")
    worksheet.write(((puzzleNumber - 1) * 9)+1, 2, "NA")
    print("Using UCS")
    resultUCS = algorithms(puzzle, fuelLevels, uniformCostSearch, "ucs")
    if resultUCS["result"] == "goal_reached":
        worksheet.write(((puzzleNumber - 1) * 9)+1, 3, len(resultUCS["state"]["solutionPath"]))
    else:
        worksheet.write(((puzzleNumber - 1) * 9)+1, 3, "No solution!")

    worksheet.write(((puzzleNumber - 1) * 9)+1, 4, resultUCS["length_search_path"])
    worksheet.write(((puzzleNumber - 1) * 9)+1, 5, float("{:.2f}".format(resultUCS["runtime"])))
    print("\n")

    #GBFS heuristic 1
    worksheet.write(((puzzleNumber - 1) * 9)+2, 0, puzzleNumber)
    worksheet.write(((puzzleNumber - 1) * 9)+2, 1, "GBFS")
    worksheet.write(((puzzleNumber - 1) * 9)+2, 2, "h1")
    print("Using GBFS heuristic 1")
    resultGBFS1 = algorithms(puzzle, fuelLevels, GBFSh1, "GBFS")

    if resultGBFS1["result"] == "goal_reached":
        worksheet.write(((puzzleNumber - 1) * 9)+2, 3, len(resultGBFS1["state"]["solutionPath"]))
    else:
        worksheet.write(((puzzleNumber - 1) * 9)+2, 3, "No solution!")

    worksheet.write(((puzzleNumber - 1) * 9)+2, 4, resultGBFS1["length_search_path"])
    worksheet.write(((puzzleNumber - 1) * 9)+2, 5, float("{:.2f}".format(resultGBFS1["runtime"])))
    print("\n")

    #GBFS heuristic 2
    worksheet.write(((puzzleNumber - 1) * 9)+3, 0, puzzleNumber)
    worksheet.write(((puzzleNumber - 1) * 9)+3, 1, "GBFS")
    worksheet.write(((puzzleNumber - 1) * 9)+3, 2, "h2")
    print("Using GBFS heuristic 2")
    resultGBFS2 = algorithms(puzzle, fuelLevels, GBFSh2, "GBFS")

    if resultGBFS2["result"] == "goal_reached":
        worksheet.write(((puzzleNumber - 1) * 9)+3, 3, len(resultGBFS2["state"]["solutionPath"]))
    else:
        worksheet.write(((puzzleNumber - 1) * 9)+3, 3, "No solution!")

    worksheet.write(((puzzleNumber - 1) * 9)+3, 4, resultGBFS2["length_search_path"])
    worksheet.write(((puzzleNumber - 1) * 9)+3, 5, float("{:.2f}".format(resultGBFS2["runtime"])))
    print("\n")

    #GBFS heuristic 3
    worksheet.write(((puzzleNumber - 1) * 9)+4, 0, puzzleNumber)
    worksheet.write(((puzzleNumber - 1) * 9)+4, 1, "GBFS")
    worksheet.write(((puzzleNumber - 1) * 9)+4, 2, "h3")
    print("Using GBFS heuristic 3")
    resultGBFS3 = algorithms(puzzle, fuelLevels, GBFSh3, "gbfs")

    if resultGBFS3["result"] == "goal_reached":
        worksheet.write(((puzzleNumber - 1) * 9)+4, 3, len(resultGBFS3["state"]["solutionPath"]))
    else:
        worksheet.write(((puzzleNumber - 1) * 9)+4, 3, "No solution!")

    worksheet.write(((puzzleNumber - 1) * 9)+4, 4, resultGBFS3["length_search_path"])
    worksheet.write(((puzzleNumber - 1) * 9)+4, 5, float("{:.2f}".format(resultGBFS3["runtime"])))
    print("\n")

    #GBFS heuristic 4
    worksheet.write(((puzzleNumber - 1) * 9)+5, 0, puzzleNumber)
    worksheet.write(((puzzleNumber - 1) * 9)+5, 1, "GBFS")
    worksheet.write(((puzzleNumber - 1) * 9)+5, 2, "h4")
    print("Using GBFS heuristic 4")
    resultGBFS4 = algorithms(puzzle, fuelLevels, GBFSh4, "gbfs")

    if resultGBFS4["result"] == "goal_reached":
        worksheet.write(((puzzleNumber - 1) * 9)+5, 3, len(resultGBFS4["state"]["solutionPath"]))
    else:
        worksheet.write(((puzzleNumber - 1) * 9)+5, 3, "No solution!")

    worksheet.write(((puzzleNumber - 1) * 9)+5, 4, resultGBFS4["length_search_path"])
    worksheet.write(((puzzleNumber - 1) * 9)+5, 5, float("{:.2f}".format(resultGBFS4["runtime"])))
    print("\n")

    #A heuristic 1
    worksheet.write(((puzzleNumber - 1) * 9)+6, 0, puzzleNumber)
    worksheet.write(((puzzleNumber - 1) * 9)+6, 1, "A/A*")
    worksheet.write(((puzzleNumber - 1) * 9)+6, 2, "h1")
    print("Using A heuristic 1")
    resultA1 = algorithms(puzzle, fuelLevels, Ah1, "a")

    if resultA1["result"] == "goal_reached":
        worksheet.write(((puzzleNumber - 1) * 9)+6, 3, len(resultA1["state"]["solutionPath"]))
    else:
        worksheet.write(((puzzleNumber - 1) * 9)+6, 3, "No solution!")

    worksheet.write(((puzzleNumber - 1) * 9)+6, 4, resultA1["length_search_path"])
    worksheet.write(((puzzleNumber - 1) * 9)+6, 5, float("{:.2f}".format(resultA1["runtime"])))
    print("\n")

    #A heuristic 2
    worksheet.write(((puzzleNumber - 1) * 9)+7, 0, puzzleNumber)
    worksheet.write(((puzzleNumber - 1) * 9)+7, 1, "A/A*")
    worksheet.write(((puzzleNumber - 1) * 9)+7, 2, "h2")
    print("Using A heuristic 2")
    resultA2 = algorithms(puzzle, fuelLevels, Ah2, "a")

    if resultA2["result"] == "goal_reached":
        worksheet.write(((puzzleNumber - 1) * 9)+7, 3, len(resultA2["state"]["solutionPath"]))
    else:
        worksheet.write(((puzzleNumber - 1) * 9)+7, 3, "No solution!")

    worksheet.write(((puzzleNumber - 1) * 9)+7, 4, resultA2["length_search_path"])
    worksheet.write(((puzzleNumber - 1) * 9)+7, 5, float("{:.2f}".format(resultA2["runtime"])))
    print("\n")

    #A heuristic 3
    worksheet.write(((puzzleNumber - 1) * 9)+8, 0, puzzleNumber)
    worksheet.write(((puzzleNumber - 1) * 9)+8, 1, "A/A*")
    worksheet.write(((puzzleNumber - 1) * 9)+8, 2, "h3")
    print("Using A heuristic 3")
    resultA3 = algorithms(puzzle, fuelLevels, Ah3, "a")

    if resultA3["result"] == "goal_reached":
        worksheet.write(((puzzleNumber - 1) * 9)+8, 3, len(resultA3["state"]["solutionPath"]))
    else:
        worksheet.write(((puzzleNumber - 1) * 9)+8, 3, "No solution!")

    worksheet.write(((puzzleNumber - 1) * 9)+8, 4, resultA3["length_search_path"])
    worksheet.write(((puzzleNumber - 1) * 9)+8, 5, float("{:.2f}".format(resultA3["runtime"])))
    print("\n")

    #A heuristic 4
    worksheet.write(((puzzleNumber - 1) * 9)+9, 0, puzzleNumber)
    worksheet.write(((puzzleNumber - 1) * 9)+9, 1, "A/A*")
    worksheet.write(((puzzleNumber - 1) * 9)+9, 2, "h4")
    print("Using A heuristic 4")
    resultA4 = algorithms(puzzle, fuelLevels, Ah4, "a")

    if resultA4["result"] == "goal_reached":
        worksheet.write(((puzzleNumber - 1) * 9)+9, 3, len(resultA4["state"]["solutionPath"]))
    else:
        worksheet.write(((puzzleNumber - 1) * 9)+9, 3, "No solution!")

    worksheet.write(((puzzleNumber - 1) * 9)+9, 4, resultA4["length_search_path"])
    worksheet.write(((puzzleNumber - 1) * 9)+9, 5, float("{:.2f}".format(resultA4["runtime"])))
    print("\n")

for puzzleElem in puzzle50RandomList:
    solvePuzzleInSpreadsheet(puzzleElem["puzzle"], puzzleElem["fuel"], puzzleElem["puzzleNum"], worksheet)

workbook.close()