""""
This file contains methods that will write the results of 50 puzzles directly to excel sheet. 
We used xlsxwriter to directly write to excel sheet.
"""


from algorithms import *
from inputPuzzle import *
from heuristics import *
import xlsxwriter


puzzles_for_excel = readpuzzle("50Puzzles.txt")

workbook = xlsxwriter.Workbook("50PuzzlesOutput.xlsx") 
result_sheet = workbook.add_worksheet()

result_sheet.write(0, 0, "Puzzle Number")
result_sheet.write(0, 1, "Algorithm")
result_sheet.write(0, 2, "Heuristic")
result_sheet.write(0, 3, "Length of the Solution")
result_sheet.write(0, 4, "Length of the Search Path")
result_sheet.write(0, 5, "Execution Time (in seconds)")


def add_results_excel(puzzle, fuel_levels, puzzle_num, result_sheet):

    print("Solving puzzle #"+str(puzzle_num)+"\n")

    #UCS
    result_sheet.write(((puzzle_num - 1) * 9)+1, 0, puzzle_num)  # 9 is for adding each puzzle after 9 rows and same starts with 0
    result_sheet.write(((puzzle_num - 1) * 9)+1, 1, "UCS")
    result_sheet.write(((puzzle_num - 1) * 9)+1, 2, "NA")

    print("Using uniform cost search")
    uniform_cost_search_result = algorithms(puzzle, fuel_levels, uniformCostSearch, "ucs")

    if uniform_cost_search_result["result"] == "goal_reached":  #If goal reached write length of solution
        result_sheet.write(((puzzle_num - 1) * 9)+1, 3, len(uniform_cost_search_result["state"]["sol_path"]))
    else:  #else write no solution
        result_sheet.write(((puzzle_num - 1) * 9)+1, 3, "no solution")

    result_sheet.write(((puzzle_num - 1) * 9)+1, 4, uniform_cost_search_result["length_search_path"]) #write length of search path
    result_sheet.write(((puzzle_num - 1) * 9)+1, 5, round(uniform_cost_search_result["runtime"], 2))  #write rounded total run time
    print("\n")

    #GBFS heuristic 1
    result_sheet.write(((puzzle_num - 1) * 9)+2, 0, puzzle_num)
    result_sheet.write(((puzzle_num - 1) * 9)+2, 1, "GBFS")
    result_sheet.write(((puzzle_num - 1) * 9)+2, 2, "h1")

    print("Using GBFS heuristic 1")
    GBFSh1_result = algorithms(puzzle, fuel_levels, GBFSh1, "GBFS")

    if GBFSh1_result["result"] == "goal_reached":   #If goal reached write length of solution
        result_sheet.write(((puzzle_num - 1) * 9)+2, 3, len(GBFSh1_result["state"]["sol_path"]))
    else:   #else write no solution
        result_sheet.write(((puzzle_num - 1) * 9)+2, 3, "no solution")

    result_sheet.write(((puzzle_num - 1) * 9)+2, 4, GBFSh1_result["length_search_path"])  #write length of search path
    result_sheet.write(((puzzle_num - 1) * 9)+2, 5, round(GBFSh1_result["runtime"], 2))  #write rounded total run time
    print("\n")

    #GBFS heuristic 2
    result_sheet.write(((puzzle_num - 1) * 9)+3, 0, puzzle_num)
    result_sheet.write(((puzzle_num - 1) * 9)+3, 1, "GBFS")
    result_sheet.write(((puzzle_num - 1) * 9)+3, 2, "h2")

    print("Using GBFS heuristic 2")
    GBFSh2_result = algorithms(puzzle, fuel_levels, GBFSh2, "GBFS")

    if GBFSh2_result["result"] == "goal_reached":
        result_sheet.write(((puzzle_num - 1) * 9)+3, 3, len(GBFSh2_result["state"]["sol_path"]))
    else:
        result_sheet.write(((puzzle_num - 1) * 9)+3, 3, "no solution")

    result_sheet.write(((puzzle_num - 1) * 9)+3, 4, GBFSh2_result["length_search_path"])
    result_sheet.write(((puzzle_num - 1) * 9)+3, 5, round(GBFSh2_result["runtime"], 2))
    print("\n")

    #GBFS heuristic 3
    result_sheet.write(((puzzle_num - 1) * 9)+4, 0, puzzle_num)
    result_sheet.write(((puzzle_num - 1) * 9)+4, 1, "GBFS")
    result_sheet.write(((puzzle_num - 1) * 9)+4, 2, "h3")
    print("Using GBFS heuristic 3")
    GBFSh3_result = algorithms(puzzle, fuel_levels, GBFSh3, "gbfs")

    if GBFSh3_result["result"] == "goal_reached":
        result_sheet.write(((puzzle_num - 1) * 9)+4, 3, len(GBFSh3_result["state"]["sol_path"]))
    else:
        result_sheet.write(((puzzle_num - 1) * 9)+4, 3, "no solution")

    result_sheet.write(((puzzle_num - 1) * 9)+4, 4, GBFSh3_result["length_search_path"])
    result_sheet.write(((puzzle_num - 1) * 9)+4, 5, round(GBFSh3_result["runtime"], 2))
    print("\n")

    #GBFS heuristic 4
    result_sheet.write(((puzzle_num - 1) * 9)+5, 0, puzzle_num)
    result_sheet.write(((puzzle_num - 1) * 9)+5, 1, "GBFS")
    result_sheet.write(((puzzle_num - 1) * 9)+5, 2, "h4")
    print("Using GBFS heuristic 4")
    GBFSh4_result = algorithms(puzzle, fuel_levels, GBFSh4, "gbfs")

    if GBFSh4_result["result"] == "goal_reached":
        result_sheet.write(((puzzle_num - 1) * 9)+5, 3, len(GBFSh4_result["state"]["sol_path"]))
    else:
        result_sheet.write(((puzzle_num - 1) * 9)+5, 3, "no solution")

    result_sheet.write(((puzzle_num - 1) * 9)+5, 4, GBFSh4_result["length_search_path"])
    result_sheet.write(((puzzle_num - 1) * 9)+5, 5, round(GBFSh4_result["runtime"], 2))
    print("\n")

    #A heuristic 1
    result_sheet.write(((puzzle_num - 1) * 9)+6, 0, puzzle_num)
    result_sheet.write(((puzzle_num - 1) * 9)+6, 1, "A/A*")
    result_sheet.write(((puzzle_num - 1) * 9)+6, 2, "h1")
    print("Using A/A* heuristic 1")
    Ah1_result = algorithms(puzzle, fuel_levels, Ah1, "a")

    if Ah1_result["result"] == "goal_reached":
        result_sheet.write(((puzzle_num - 1) * 9)+6, 3, len(Ah1_result["state"]["sol_path"]))
    else:
        result_sheet.write(((puzzle_num - 1) * 9)+6, 3, "no solution")

    result_sheet.write(((puzzle_num - 1) * 9)+6, 4, Ah1_result["length_search_path"])
    result_sheet.write(((puzzle_num - 1) * 9)+6, 5, round(Ah1_result["runtime"], 2))
    print("\n")

    #A heuristic 2
    result_sheet.write(((puzzle_num - 1) * 9)+7, 0, puzzle_num)
    result_sheet.write(((puzzle_num - 1) * 9)+7, 1, "A/A*")
    result_sheet.write(((puzzle_num - 1) * 9)+7, 2, "h2")
    print("Using A/A* heuristic 2")
    Ah2_result = algorithms(puzzle, fuel_levels, Ah2, "a")

    if Ah2_result["result"] == "goal_reached":
        result_sheet.write(((puzzle_num - 1) * 9)+7, 3, len(Ah2_result["state"]["sol_path"]))
    else:
        result_sheet.write(((puzzle_num - 1) * 9)+7, 3, "no solution")

    result_sheet.write(((puzzle_num - 1) * 9)+7, 4, Ah2_result["length_search_path"])
    result_sheet.write(((puzzle_num - 1) * 9)+7, 5, round(Ah2_result["runtime"], 2))
    print("\n")

    #A heuristic 3
    result_sheet.write(((puzzle_num - 1) * 9)+8, 0, puzzle_num)
    result_sheet.write(((puzzle_num - 1) * 9)+8, 1, "A/A*")
    result_sheet.write(((puzzle_num - 1) * 9)+8, 2, "h3")
    print("Using A/A* heuristic 3")
    Ah3_result = algorithms(puzzle, fuel_levels, Ah3, "a")

    if Ah3_result["result"] == "goal_reached":
        result_sheet.write(((puzzle_num - 1) * 9)+8, 3, len(Ah3_result["state"]["sol_path"]))
    else:
        result_sheet.write(((puzzle_num - 1) * 9)+8, 3, "no solution")

    result_sheet.write(((puzzle_num - 1) * 9)+8, 4, Ah3_result["length_search_path"])
    result_sheet.write(((puzzle_num - 1) * 9)+8, 5, round(Ah3_result["runtime"], 2))
    print("\n")

    #A heuristic 4
    result_sheet.write(((puzzle_num - 1) * 9)+9, 0, puzzle_num)
    result_sheet.write(((puzzle_num - 1) * 9)+9, 1, "A/A*")
    result_sheet.write(((puzzle_num - 1) * 9)+9, 2, "h4")
    print("Using A/A* heuristic 4")
    Ah4_result = algorithms(puzzle, fuel_levels, Ah4, "a")

    if Ah4_result["result"] == "goal_reached":
        result_sheet.write(((puzzle_num - 1) * 9)+9, 3, len(Ah4_result["state"]["sol_path"]))
    else:
        result_sheet.write(((puzzle_num - 1) * 9)+9, 3, "no solution")

    result_sheet.write(((puzzle_num - 1) * 9)+9, 4, Ah4_result["length_search_path"])
    result_sheet.write(((puzzle_num - 1) * 9)+9, 5, round(Ah4_result["runtime"], 2))
    print("\n")

for each_puzzle in puzzles_for_excel: 
    add_results_excel(each_puzzle["puzzle"], each_puzzle["fuel"], each_puzzle["puzzleNum"], result_sheet)


workbook.close()
