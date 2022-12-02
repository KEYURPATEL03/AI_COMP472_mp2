def goalTest(puzzle):  # This function will be called when a node/board is created to check if it is goal.
    if puzzle[2][4] == "A" and puzzle[2][5] == "A":  # This will check if ambulance is on exit position
        return True
    return False


def valetService(puzzle):    #This will run mandatory valet service on every puzzle for free of cost
    if puzzle[2][5] != "A" and puzzle[2][5] != ".":

        i = 4
        while i >= 2:                           #This will only run this position 2 of row 2 because we need two places for ambulance
            if puzzle[2][i] == puzzle[2][5]:
                puzzle[2][i] = "."
            else:
                break

            i -= 1

    return puzzle
