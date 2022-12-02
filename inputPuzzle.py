def readpuzzle(file):
    list_of_puzzle = []  # an array to store the list of puzzle
    file_input = open(file, 'r')
    lines = file_input.readlines()
    puzzle_num = 1  # initially the number of puzzle is 1 , will increment as reading the file

    for line in lines:
        fuels = {}
        puzzle = []  # an array to store a single puzzle
        line = line.strip()  # Removes any leading(space in beginning) & trailing (spaces at the end)

        # 2. an empty line (useful for formatting) – you should skip that line
        # 3. a line that starts with a # (useful for inserting comments) – you should skip this line also.
        if line != "" and not line.startswith("#"):
            splitlines = line.split(" ")
            string_Of_Puzzle = splitlines[0]

            puzzle_row = []
            for i in range(len(string_Of_Puzzle)):

                if string_Of_Puzzle[i] not in fuels and string_Of_Puzzle != ".":
                    fuels[string_Of_Puzzle[i]] = 100  # 1. if no fuel level is indicated,assuming the vehicle has a fuel level of 100
                puzzle_row.append(string_Of_Puzzle[i])
                if len(puzzle_row) == 6:
                    puzzle.append(puzzle_row)
                    puzzle_row = []

            array_of_fuel = splitlines[1:]
            for fuel in array_of_fuel:
                fuels[fuel[0]] = int(fuel[1])

            list_of_puzzle.append({"puzzle_num": puzzle_num,
                                   "string_Of_Puzzle": string_Of_Puzzle,
                                   "puzzle": puzzle,
                                   "fuel": fuels})
            puzzle_num += 1

    file_input.close()
    return list_of_puzzle


puzzle_list = readpuzzle('sample-input.txt')
print(puzzle_list)
