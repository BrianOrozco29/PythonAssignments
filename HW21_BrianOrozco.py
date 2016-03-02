''' contributions of possible winning triplets to boardVal '''
x3 = 1000
x2 = 50
x1 = 10
o3 = -1000
o2 = -50
o1 = -10


def getComputerMove(player, board): #get move iz da sam
    ''' Evaluate the board resulting from each possible
    move. Return the highest value if player == 'X', the
    lowest value if player == 'O'.'''

def getBestVal(player, outcomes):
    ''' Player is 'X' or 'O'. outcomes is a dictionary in which each key
    is a move, and its value is the corresponding value of the board.
    Create a list of best moves (max for X, min for O). If there is
    a single best value, return that move. In case of a tie, pick among
    the equally good moves at random. '''

def evalBoard(board): 
    ''' Compute and return the value of the board, using the global
    values assigned to each possible configuration of the 8 possible
    winning triplets. '''
    triplets = (
    [0,1,2],[3,4,5],[6,7,8],  # horizontals
    [0,3,6],[1,4,7],[2,5,8],  # verticals
    [0,4,8],[6,4,2]           # diagonals
    )

    oValue = 0
    for triple in triplets:
        boardLetters=[board[triple[0]],board[triple[1]],board[triple[2]]]
        if boardLetters[0] == 'O' and boardLetters[1] == 'O' and boardLetters[2] == 'O':
            oValue += o3
            return oValue
        elif boardLetters[0] == 'O' and boardLetters[1] == 'O' and boardLetters[2] != 'X':
            oValue += o2
        elif boardLetters[1] == 'O' and boardLetters[2]=='O' and boardLetters[0] != 'X':
            oValue += o2
        elif boardLetters[0] == 'O' and boardLetters[2]=='O' and boardLetters[1] != 'X':
            oValue += o2
        elif boardLetters.count('O') == 1:
            oValue += o1
    
    xValue = 0  
    for triple in triplets:
        boardLetters=[board[triple[0]],board[triple[1]],board[triple[2]]]
        if boardLetters[0]=='X' and boardLetters[1] == 'X' and boardLetters[2] == 'X':
            xValue += x3
            return xValue
        elif boardLetters[0] == 'X' and boardLetters[1] == 'X' and boardLetters[2] != 'O':
            xValue += x2
        elif boardLetters[1] == 'X' and boardLetters[2] == 'X' and boardLetters[0] != 'O':
            xValue += x2
        elif boardLetters[0] == 'X' and boardLetters[2] == 'X' and boardLetters[1] != 'O':
            xValue += x2
        elif boardLetters.count('X') == 1:
            xValue += x1
            
    return oValue


board1=['X', 'X', 'O', '-', 'O', 'X', 'O', '-', '-']
board2=['-', 'X', 'O', '-', 'X', 'O', '-', 'O', 'X']
board3=['X', 'X', 'O', '-', 'X', 'O', '-', 'O', 'X']
board4=['X', '-', 'O', '-', 'X', 'O', '-', 'X', '-']
board5=['O', 'X', 'O', 'O', 'X', 'X', 'X', 'O', 'X']

print("Board 1 " + str(evalBoard(board1)))
print(board1)
print()
print("Board 2 " + str(evalBoard(board2)))
print(board2)
print()
print("Board 3 " + str(evalBoard(board3)))
print(board3)
print()
print("Board 4 " + str(evalBoard(board4)))
print(board4)
print()
print("Board 5 " + str(evalBoard(board5)))
print(board5)
        
            
        
