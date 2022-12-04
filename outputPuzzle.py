""""
This file contains methods that will output the results of search and solution path to a file. The input
file is sample-input.txt
"""


from algorithms import *
from inputPuzzle import *
from heuristics import *


def create_solution_file(result, string_config, algo, puzzle_num, fuel_levels):
    
    solution_file = open("./output_files/solution_files/"+algo + "sol-" + str(puzzle_num) + ".txt", "w")
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
        for key in fuel_levels:
            solution_file.write(str(key) + ":" + str(fuel_levels[key]) + ", ")

        solution_file.write("\n\n")

        solution_file.write("Runtime: " + str(round(result["runtime"], 2)) + " seconds\n")  #This will write run time rounded to two decimal
        solution_file.write("Search path length: " + str(result["length_search_path"]) + "\n")  #This will write search path length
        solution_file.write("Solution path length: " + str(len(result["state"]["sol_path"])) + "\n")  #This will write solution path length

        solution_file.write("Solution path: ")     #This will write the solution path
        for path in result["state"]["sol_path"]:
            solution_file.write(" " + path["carType"] + " " + path["direction"] + str(path["displacement"]) + ";")
        solution_file.write("\n\n")

        for path in result["state"]["sol_path"]:        #This will print puzzle after each move

            solution_file.write("\n" + path["carType"] + " " + path["direction"] + str(path["displacement"]) + "     " + str(path["fuel_levels"][path["carType"]]) + "  ")
            
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
        for key in fuel_levels:
            solution_file.write(str(key) + ":" + str(fuel_levels[key]) + ", ")
        solution_file.write("\n\n")

        solution_file.write("No solution\n\n")
    solution_file.close()


def create_search_file(result, algo, puzzle_num):
    search_file = open("./output_files/search_files/" + algo+"search-"+str(puzzle_num)+".txt", "w")
    close_list = result["close_list"]                   #copy whole close list to print the search path
    for state in close_list:

        if "ucs" in algo:        # If algorithm is UCS, write g(n)
            search_file.write("0 " + str(state["Fn"]) + " 0 ")

        elif "gbfs" in algo:         # If algorithm is GBFS, write h(n)
            search_file.write("0 0" + str(state["Fn"]) + " ")

        else:   # f(n) g(n) h(n)
            Hn = state["Fn"] - len(state["sol_path"])    ## If algorithm is A/A*, write f(n)
            search_file.write(str(state["Fn"]) + " " + str(len(state["sol_path"])) + " " + str(Hn) + " ")

        for row in state["puzzle"]:
            for column in row:
                search_file.write(column)

        search_file.write(" \n")

    search_file.close()


# ----------------------------------------------------------------------------------------------------------------------------


def solvePuzzle(puzzle, fuels, string_config, puzzle_num):  # main function; call algorithm function for all puzzles

    print("Solving puzzle #" + str(puzzle_num))     # uniform cost search
    print("Using uniform cost search")
    uniform_cost_search_result = algorithms(puzzle, fuels, uniformCostSearch, "ucs")
    create_solution_file(uniform_cost_search_result, string_config, "ucs-", puzzle_num, fuels)
    create_search_file(uniform_cost_search_result, "ucs-", puzzle_num)
    print("\n")

    print("Using GBFS heuristic 1")      # GBFS heuristic 1
    GBFSh1_result = algorithms(puzzle, fuels, GBFSh1, "gbfs")
    create_solution_file(GBFSh1_result, string_config, "gbfs-h1-", puzzle_num, fuels)
    create_search_file(GBFSh1_result, "gbfs-h1-", puzzle_num)
    print("\n")

    print("Using GBFS heuristic 2")         # GBFS heuristic 2
    GBFSh2_result = algorithms(puzzle, fuels, GBFSh2, "gbfs")
    create_solution_file(GBFSh2_result, string_config, "gbfs-h2-", puzzle_num, fuels)
    create_search_file(GBFSh2_result, "gbfs-h2-", puzzle_num)
    print("\n")

    print("Using GBFS heuristic 3")   # GBFS heuristic 3
    GBFSh3_result = algorithms(puzzle, fuels, GBFSh3, "gbfs")
    create_solution_file(GBFSh3_result, string_config, "gbfs-h3-", puzzle_num, fuels)
    create_search_file(GBFSh3_result, "gbfs-h3-", puzzle_num)
    print("\n")

    print("Using GBFS heuristic 4") # GBFS heuristic 4
    GBFSh4_result = algorithms(puzzle, fuels, GBFSh4, "gbfs")
    create_solution_file(GBFSh4_result, string_config, "gbfs-h4-", puzzle_num, fuels)
    create_search_file(GBFSh4_result, "gbfs-h4-", puzzle_num)
    print("\n")

    print("Using A/A* heuristic 1")     # A heuristic 1
    Ah1_result = algorithms(puzzle, fuels, Ah1, "a")
    create_solution_file(Ah1_result, string_config, "a-h1-", puzzle_num, fuels)
    create_search_file(Ah1_result, "a-h1-", puzzle_num)
    print("\n")

    print("Using A/A* heuristic 2")     # A heuristic 2
    Ah2_result = algorithms(puzzle, fuels, Ah2, "a")
    create_solution_file(Ah2_result, string_config, "a-h2-", puzzle_num, fuels)
    create_search_file(Ah2_result, "a-h2-", puzzle_num)
    print("\n")

    print("Using A/A* heuristic 3") # A heuristic 3
    Ah3_result = algorithms(puzzle, fuels, Ah3, "a")
    create_solution_file(Ah3_result, string_config, "a-h3-", puzzle_num, fuels)
    create_search_file(Ah3_result, "a-h3-", puzzle_num)
    print("\n")

    print("Using A/A* heuristic 4") # A heuristic 4
    Ah4_result = algorithms(puzzle, fuels, Ah4, "a")
    create_solution_file(Ah4_result, string_config, "a-h4-", puzzle_num, fuels)
    create_search_file(Ah4_result, "a-h4-", puzzle_num)
    print("\n")


puzzleList = readpuzzle("sample-input.txt")
for each_puzzle in puzzleList:
    solvePuzzle(each_puzzle["puzzle"], each_puzzle["fuel"], each_puzzle["string_of_puzzle"], each_puzzle["puzzle_num"])
