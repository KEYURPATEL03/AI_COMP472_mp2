def readpuzzle(file):
    list_of_puzzle = []  # an array to store the list of puzzle
    file_input = open(file, 'r')
    lines = file_input.readlines()
    puzzle_num = 1  # initially the number of puzzle is 1 , will increment as reading the file

    for line in lines:
        fuels = {}
        puzzle = []     # an array to store a single puzzle
        line = line.strip()  # Removes any leading(space in beginning) & trailing (spaces at the end)

        # 2. an empty line (useful for formatting) – you should skip that line
        # 3. a line that starts with a # (useful for inserting comments) – you should skip this line also.
        if line != "" and not line.startswith("#"):
            splitlines = line.split(" ")
            string_Of_Puzzle = splitlines[0]

            puzzle_row = []  # initializing an empty array puzzle row!
            for i in range(len(string_Of_Puzzle)):   # running this for loop until the 36 characters of the board

                if string_Of_Puzzle[i] not in fuels and string_Of_Puzzle[i] != '.':  # '.' should not have any fuel as it is not a car
                    fuels[string_Of_Puzzle[i]] = 100  # 1. if no fuel level is indicated,assuming the vehicle has a fuel level of 100
                puzzle_row.append(string_Of_Puzzle[i])  # appending the default fuel of each car
                if len(puzzle_row) == 6:   # breaking the string of puzzle after 6 characters
                    puzzle.append(puzzle_row)
                    puzzle_row = []  # this to put first row of the board into the array.
                # end of loop
            arrayoffuel = splitlines[1:]
            for fuel in arrayoffuel:        # this for loop for accessing the fuel level after the 36 characters of the board!
                fuels[fuel[0]] = int(fuel[1])
                # end of loop
            # Now appending everything together  to get a single puzzle
            list_of_puzzle.append({"puzzle": puzzle, "fuel": fuels, "stringOfPuzzle": string_Of_Puzzle, "puzzleNum": puzzle_num})
            print("\n")
            print("puzzleNum:", puzzle_num)
            print("stringOfPuzzle:", string_Of_Puzzle)
            print("puzzle:", puzzle)
            print("fuel:", fuels)

            puzzle_num = puzzle_num + 1
    # end of loop
    file_input.close()
    return list_of_puzzle


puzzlelist = readpuzzle('sample-input.txt')

