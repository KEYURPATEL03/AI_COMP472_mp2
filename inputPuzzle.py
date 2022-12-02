def readpuzzle(file):
    listofpuzzle = []  # an array to store the list of puzzle
    file_input = open(file, 'r')
    lines = file_input.readlines()
    puzzlenum = 1  # initially the number of puzzle is 1 , will increment as reading the file

    for line in lines:
        fuels = {}
        puzzle = []     # an array to store a single puzzle
        line = line.strip()  # Removes any leading(space in beginning) & trailing (spaces at the end)

        # 2. an empty line (useful for formatting) – you should skip that line
        # 3. a line that starts with a # (useful for inserting comments) – you should skip this line also.
        if line != "" and not line.startswith("#"):
            splitlines = line.split(" ")
            stringofpuzzle = splitlines[0]

            puzzlerow = []
            for i in range(len(stringofpuzzle)):

                if stringofpuzzle[i] not in fuels and stringofpuzzle != ".":
                    fuels[stringofpuzzle[i]] = 100  # 1. if no fuel level is indicated,assuming the vehicle has a fuel level of 100
                puzzlerow.append(stringofpuzzle[i])
                if len(puzzlerow) == 6:
                    puzzle.append(puzzlerow)
                    puzzlerow = []

            arrayoffuel = splitlines[1:]
            for fuel in arrayoffuel:
                fuels[fuel[0]] = int(fuel[1])

            listofpuzzle.append({"puzzleNum": puzzlenum, "stringOfPuzzle": stringofpuzzle, "puzzle": puzzle, "fuel": fuels})
            puzzlenum = puzzlenum + 1

    file_input.close()
    return listofpuzzle


puzzlelist = readpuzzle('sample-input.txt')

