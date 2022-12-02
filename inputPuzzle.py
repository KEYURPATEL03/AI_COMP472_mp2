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

            puzzlerow = []  # initializing an empty array puzzle row!
            for i in range(len(stringofpuzzle)):   # running this for loop until the 36 characters of the board

                if stringofpuzzle[i] not in fuels and stringofpuzzle[i] != '.':  # '.' should not have any fuel as it is not a car
                    fuels[stringofpuzzle[i]] = 100  # 1. if no fuel level is indicated,assuming the vehicle has a fuel level of 100
                puzzlerow.append(stringofpuzzle[i])  # appending the default fuel of each car
                if len(puzzlerow) == 6:   # breaking the string of puzzle after 6 characters
                    puzzle.append(puzzlerow)
                    puzzlerow = []  # this to put first row of the board into the array.
                # end of loop
            arrayoffuel = splitlines[1:]
            for fuel in arrayoffuel:        # this for loop for accessing the fuel level after the 36 characters of the board!
                fuels[fuel[0]] = int(fuel[1])
                # end of loop
            # Now appending everything together  to get a single puzzle
            listofpuzzle.append({"puzzleNum": puzzlenum, "stringOfPuzzle": stringofpuzzle, "puzzle": puzzle, "fuel": fuels})
            print("\n")
            print("puzzleNum:", puzzlenum)
            print("stringofpuzzle:", stringofpuzzle)
            print("puzzle:", puzzle)
            print("fuel:", fuels)

            puzzlenum = puzzlenum + 1
    # end of loop
    file_input.close()
    return listofpuzzle


puzzlelist = readpuzzle('sample-input.txt')
