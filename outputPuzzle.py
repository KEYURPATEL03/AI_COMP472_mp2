from algorithms import *
from inputPuzzle import *
from heuristics import *
import xlsxwriter


def create_solution_file(result, string_config, algo, puzzle_num, fuelLevels):
    
    solution_file = open(algo + "sol-" + str(puzzle_num) + ".txt", "w")
    if result["result"] == "goal_reached":      
        solution_file.write("Initial board configuration: " + string_config + "\n\n")

        j = 0
        for i in range(len(string_config)):              #This will write the string configuration as matrix
            solution_file.write(string_config[i] + " ")
            j += 1
            if j == 6:
                solution_file.write("\n")
                j = 0
        solution_file.write("\n")

        solution_file.write("Car fuel available: ")     #This will write the initial fuels of all the cars
        for key in fuelLevels:
            solution_file.write(str(key) + ":" + str(fuelLevels[key]) + ", ")

        solution_file.write("\n\n")

        solution_file.write("Runtime: " + str(round(result["runtime"], 2)) + " seconds\n")  #This will write run time rounded to two decimal
        solution_file.write("Search path length: " + str(result["length_search_path"]) + "\n")  #This will write search path length
        solution_file.write("Solution path length: " + str(len(result["state"]["solutionPath"])) + "\n")  #This will write solution path length

        solution_file.write("Solution path: ")     #This will write the solution path
        for path in result["state"]["solutionPath"]:
            solution_file.write(" " + path["carType"] + " " + path["direction"] + str(path["displacement"]) + ";")
        solution_file.write("\n\n")

        for path in result["state"]["solutionPath"]:        #This will print puzzle after each move

            solution_file.write("\n" + path["carType"] + " " + path["direction"] + str(path["displacement"]) + "     " + str(path["fuelLevels"][path["carType"]]) + "  ")
            
            for row in path["puzzle"]:
                for column in row:
                    solution_file.write(column)
        solution_file.write("\n\n")

        final_puzzle = result["state"]["puzzle"]

        for row in final_puzzle:
            for column in row:
                solution_file.write(column + " ")
            solution_file.write("\n")

    else:
        # The else will be executed if there is no solution
        solution_file.write("Initial board configuration: " + string_config + "\n\n")

        j = 0
        for i in range(len(string_config)):              #This will write the string configuration as matrix
            solution_file.write(string_config[i] + " ")
            j += 1
            if j == 6:
                solution_file.write("\n")
                j = 0
        solution_file.write("\n")

        solution_file.write("Car fuel available: ")     #This will write the initial fuels of all the cars
        for key in fuelLevels:
            solution_file.write(str(key) + ":" + str(fuelLevels[key]) + ", ")
        solution_file.write("\n\n")

        solution_file.write("No solution\n\n")
    solution_file.close()


def create_search_file(result, string_config, algo, puzzle_num):
    search_file = open(algo+"search-"+str(puzzle_num)+".txt", "w")
    close_list = result["close_list"]                   #copy whole close list to print the search path
    for state in close_list:

        if algo.__contains__("ucs"):        # If algorithm is UCS, write g(n)
            search_file.write("0 " + str(state["Fn"]) + " 0 ")

        elif algo.__contains__("gbfs"):         # If algorithm is GBFS, write h(n)
            search_file.write("0 0" + str(state["Fn"]) + " ")

        else:   # f(n) g(n) h(n)
            Hn = state["Fn"] - len(state["solutionPath"])    ## If algorithm is A/A*, write f(n)
            search_file.write(str(state["Fn"]) + " " + str(len(state["solutionPath"])) + " " + str(Hn) + " ")

        for row in state["puzzle"]:
            for column in row:
                search_file.write(column)

        search_file.write(" \n")

    search_file.close()


# ----------------------------------------------------------------------------------------------------------------------------


def solvePuzzle(puzzle, fuels, string_config, puzzle_num):  # main function; call algorithm function for all puzzles

    # uniform cost search
    print("Solving puzzle #" + str(puzzle_num))
    print("Using uniform cost search")
    uniform_cost_search_result = algorithms(puzzle, fuels, uniformCostSearch, "ucs")
    create_solution_file(uniform_cost_search_result, string_config, "ucs-", puzzle_num, fuels)
    create_search_file(uniform_cost_search_result, string_config, "ucs-", puzzle_num)
    print("\n")

    # GBFS heuristic 1
    print("Using GBFS heuristic 1")
    GBFSh1_result = algorithms(puzzle, fuels, GBFSh1, "gbfs")
    create_solution_file(GBFSh1_result, string_config, "gbfs-h1-", puzzle_num, fuels)
    create_search_file(GBFSh1_result, string_config, "gbfs-h1-", puzzle_num)
    print("\n")

    # GBFS heuristic 2
    print("Using GBFS heuristic 2")
    GBFSh2_result = algorithms(puzzle, fuels, GBFSh2, "gbfs")
    create_solution_file(GBFSh2_result, string_config, "gbfs-h2-", puzzle_num, fuels)
    create_search_file(GBFSh2_result, string_config, "gbfs-h2-", puzzle_num)
    print("\n")

    # GBFS heuristic 3
    print("Using GBFS heuristic 3")
    GBFSh3_result = algorithms(puzzle, fuels, GBFSh3, "gbfs")
    create_solution_file(GBFSh3_result, string_config, "gbfs-h3-", puzzle_num, fuels)
    create_search_file(GBFSh3_result, string_config, "gbfs-h3-", puzzle_num)
    print("\n")

    # GBFS heuristic 4
    print("Using GBFS heuristic 4")
    GBFSh4_result = algorithms(puzzle, fuels, GBFSh4, "gbfs")
    create_solution_file(GBFSh4_result, string_config, "gbfs-h4-", puzzle_num, fuels)
    create_search_file(GBFSh4_result, string_config, "gbfs-h4-", puzzle_num)
    print("\n")

    # A heuristic 1
    print("Using A/A* heuristic 1")
    Ah1_result = algorithms(puzzle, fuels, Ah1, "a")
    create_solution_file(Ah1_result, string_config, "a-h1-", puzzle_num, fuels)
    create_search_file(Ah1_result, string_config, "a-h1-", puzzle_num)
    print("\n")

    # A heuristic 2
    print("Using A/A* heuristic 2")
    Ah2_result = algorithms(puzzle, fuels, Ah2, "a")
    create_solution_file(Ah2_result, string_config, "a-h2-", puzzle_num, fuels)
    create_search_file(Ah2_result, string_config, "a-h2-", puzzle_num)
    print("\n")

    # A heuristic 3
    print("Using A/A* heuristic 3")
    Ah3_result = algorithms(puzzle, fuels, Ah3, "a")
    create_solution_file(Ah3_result, string_config, "a-h3-", puzzle_num, fuels)
    create_search_file(Ah3_result, string_config, "a-h3-", puzzle_num)
    print("\n")

    # A heuristic 4
    print("Using A/A* heuristic 4")
    Ah4_result = algorithms(puzzle, fuels, Ah4, "a")
    create_solution_file(Ah4_result, string_config, "a-h4-", puzzle_num, fuels)
    create_search_file(Ah4_result, string_config, "a-h4-", puzzle_num)
    print("\n")
# ---------------------------------------------------------------------------------------------------------------------
puzzleList = readpuzzle("sample-input.txt")
for column in puzzleList:
    solvePuzzle(column["puzzle"], column["fuel"], column["string_of_puzzle"], column["puzzle_num"])

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

def solvePuzzleInSpreadsheet(puzzle, fuelLevels, puzzle_num, worksheet):

    print("Solving puzzle #"+str(puzzle_num)+"\n")

    #UCS
    worksheet.write(((puzzle_num - 1) * 9)+1, 0, puzzle_num)
    worksheet.write(((puzzle_num - 1) * 9)+1, 1, "UCS")
    worksheet.write(((puzzle_num - 1) * 9)+1, 2, "NA")
    print("Using UCS")
    uniform_cost_search_result = algorithms(puzzle, fuelLevels, uniformCostSearch, "ucs")
    if uniform_cost_search_result["result"] == "goal_reached":
        worksheet.write(((puzzle_num - 1) * 9)+1, 3, len(uniform_cost_search_result["state"]["solutionPath"]))
    else:
        worksheet.write(((puzzle_num - 1) * 9)+1, 3, "No solution!")

    worksheet.write(((puzzle_num - 1) * 9)+1, 4, uniform_cost_search_result["length_search_path"])
    worksheet.write(((puzzle_num - 1) * 9)+1, 5, float("{:.2f}".format(uniform_cost_search_result["runtime"])))
    print("\n")

    #GBFS heuristic 1
    worksheet.write(((puzzle_num - 1) * 9)+2, 0, puzzle_num)
    worksheet.write(((puzzle_num - 1) * 9)+2, 1, "GBFS")
    worksheet.write(((puzzle_num - 1) * 9)+2, 2, "h1")
    print("Using GBFS heuristic 1")
    GBFSh1_result = algorithms(puzzle, fuelLevels, GBFSh1, "GBFS")

    if GBFSh1_result["result"] == "goal_reached":
        worksheet.write(((puzzle_num - 1) * 9)+2, 3, len(GBFSh1_result["state"]["solutionPath"]))
    else:
        worksheet.write(((puzzle_num - 1) * 9)+2, 3, "No solution!")

    worksheet.write(((puzzle_num - 1) * 9)+2, 4, GBFSh1_result["length_search_path"])
    worksheet.write(((puzzle_num - 1) * 9)+2, 5, float("{:.2f}".format(GBFSh1_result["runtime"])))
    print("\n")

    #GBFS heuristic 2
    worksheet.write(((puzzle_num - 1) * 9)+3, 0, puzzle_num)
    worksheet.write(((puzzle_num - 1) * 9)+3, 1, "GBFS")
    worksheet.write(((puzzle_num - 1) * 9)+3, 2, "h2")
    print("Using GBFS heuristic 2")
    GBFSh2_result = algorithms(puzzle, fuelLevels, GBFSh2, "GBFS")

    if GBFSh2_result["result"] == "goal_reached":
        worksheet.write(((puzzle_num - 1) * 9)+3, 3, len(GBFSh2_result["state"]["solutionPath"]))
    else:
        worksheet.write(((puzzle_num - 1) * 9)+3, 3, "No solution!")

    worksheet.write(((puzzle_num - 1) * 9)+3, 4, GBFSh2_result["length_search_path"])
    worksheet.write(((puzzle_num - 1) * 9)+3, 5, float("{:.2f}".format(GBFSh2_result["runtime"])))
    print("\n")

    #GBFS heuristic 3
    worksheet.write(((puzzle_num - 1) * 9)+4, 0, puzzle_num)
    worksheet.write(((puzzle_num - 1) * 9)+4, 1, "GBFS")
    worksheet.write(((puzzle_num - 1) * 9)+4, 2, "h3")
    print("Using GBFS heuristic 3")
    GBFSh3_result = algorithms(puzzle, fuelLevels, GBFSh3, "gbfs")

    if GBFSh3_result["result"] == "goal_reached":
        worksheet.write(((puzzle_num - 1) * 9)+4, 3, len(GBFSh3_result["state"]["solutionPath"]))
    else:
        worksheet.write(((puzzle_num - 1) * 9)+4, 3, "No solution!")

    worksheet.write(((puzzle_num - 1) * 9)+4, 4, GBFSh3_result["length_search_path"])
    worksheet.write(((puzzle_num - 1) * 9)+4, 5, float("{:.2f}".format(GBFSh3_result["runtime"])))
    print("\n")

    #GBFS heuristic 4
    worksheet.write(((puzzle_num - 1) * 9)+5, 0, puzzle_num)
    worksheet.write(((puzzle_num - 1) * 9)+5, 1, "GBFS")
    worksheet.write(((puzzle_num - 1) * 9)+5, 2, "h4")
    print("Using GBFS heuristic 4")
    GBFSh4_result = algorithms(puzzle, fuelLevels, GBFSh4, "gbfs")

    if GBFSh4_result["result"] == "goal_reached":
        worksheet.write(((puzzle_num - 1) * 9)+5, 3, len(GBFSh4_result["state"]["solutionPath"]))
    else:
        worksheet.write(((puzzle_num - 1) * 9)+5, 3, "No solution!")

    worksheet.write(((puzzle_num - 1) * 9)+5, 4, GBFSh4_result["length_search_path"])
    worksheet.write(((puzzle_num - 1) * 9)+5, 5, float("{:.2f}".format(GBFSh4_result["runtime"])))
    print("\n")

    #A heuristic 1
    worksheet.write(((puzzle_num - 1) * 9)+6, 0, puzzle_num)
    worksheet.write(((puzzle_num - 1) * 9)+6, 1, "A/A*")
    worksheet.write(((puzzle_num - 1) * 9)+6, 2, "h1")
    print("Using A heuristic 1")
    Ah1_result = algorithms(puzzle, fuelLevels, Ah1, "a")

    if Ah1_result["result"] == "goal_reached":
        worksheet.write(((puzzle_num - 1) * 9)+6, 3, len(Ah1_result["state"]["solutionPath"]))
    else:
        worksheet.write(((puzzle_num - 1) * 9)+6, 3, "No solution!")

    worksheet.write(((puzzle_num - 1) * 9)+6, 4, Ah1_result["length_search_path"])
    worksheet.write(((puzzle_num - 1) * 9)+6, 5, float("{:.2f}".format(Ah1_result["runtime"])))
    print("\n")

    #A heuristic 2
    worksheet.write(((puzzle_num - 1) * 9)+7, 0, puzzle_num)
    worksheet.write(((puzzle_num - 1) * 9)+7, 1, "A/A*")
    worksheet.write(((puzzle_num - 1) * 9)+7, 2, "h2")
    print("Using A heuristic 2")
    Ah2_result = algorithms(puzzle, fuelLevels, Ah2, "a")

    if Ah2_result["result"] == "goal_reached":
        worksheet.write(((puzzle_num - 1) * 9)+7, 3, len(Ah2_result["state"]["solutionPath"]))
    else:
        worksheet.write(((puzzle_num - 1) * 9)+7, 3, "No solution!")

    worksheet.write(((puzzle_num - 1) * 9)+7, 4, Ah2_result["length_search_path"])
    worksheet.write(((puzzle_num - 1) * 9)+7, 5, float("{:.2f}".format(Ah2_result["runtime"])))
    print("\n")

    #A heuristic 3
    worksheet.write(((puzzle_num - 1) * 9)+8, 0, puzzle_num)
    worksheet.write(((puzzle_num - 1) * 9)+8, 1, "A/A*")
    worksheet.write(((puzzle_num - 1) * 9)+8, 2, "h3")
    print("Using A heuristic 3")
    Ah3_result = algorithms(puzzle, fuelLevels, Ah3, "a")

    if Ah3_result["result"] == "goal_reached":
        worksheet.write(((puzzle_num - 1) * 9)+8, 3, len(Ah3_result["state"]["solutionPath"]))
    else:
        worksheet.write(((puzzle_num - 1) * 9)+8, 3, "No solution!")

    worksheet.write(((puzzle_num - 1) * 9)+8, 4, Ah3_result["length_search_path"])
    worksheet.write(((puzzle_num - 1) * 9)+8, 5, float("{:.2f}".format(Ah3_result["runtime"])))
    print("\n")

    #A heuristic 4
    worksheet.write(((puzzle_num - 1) * 9)+9, 0, puzzle_num)
    worksheet.write(((puzzle_num - 1) * 9)+9, 1, "A/A*")
    worksheet.write(((puzzle_num - 1) * 9)+9, 2, "h4")
    print("Using A heuristic 4")
    Ah4_result = algorithms(puzzle, fuelLevels, Ah4, "a")

    if Ah4_result["result"] == "goal_reached":
        worksheet.write(((puzzle_num - 1) * 9)+9, 3, len(Ah4_result["state"]["solutionPath"]))
    else:
        worksheet.write(((puzzle_num - 1) * 9)+9, 3, "No solution!")

    worksheet.write(((puzzle_num - 1) * 9)+9, 4, Ah4_result["length_search_path"])
    worksheet.write(((puzzle_num - 1) * 9)+9, 5, float("{:.2f}".format(Ah4_result["runtime"])))
    print("\n")

for puzzleElem in puzzle50RandomList:
    solvePuzzleInSpreadsheet(puzzleElem["puzzle"], puzzleElem["fuel"], puzzleElem["puzzleNum"], worksheet)

workbook.close()