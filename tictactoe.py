"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    if board == [[EMPTY, EMPTY, EMPTY],
                 [EMPTY, EMPTY, EMPTY],
                 [EMPTY, EMPTY, EMPTY]] :

                 return X
    
    numOfX = 0
    numOfO = 0
    for row in board:
        for entry in row:
            if entry == X:
                numOfX += 1
            elif entry == O:
                numOfO += 1


    if numOfX > numOfO:
        return O
    
    else:
        return X

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    allActions = set()

    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                postion = (i, j)
                allActions.add(postion)

    return allActions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    row, cell = action

    if notValidAction(action) or board[row][cell] != EMPTY:
        raise Exception("Not a valid action")   

    Player = player(board)

    copy = deepCopy(board)

    copy[row][cell] = Player

    return copy


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # Check first horizontal row
    cell = board[0][0]
    Horizontal = True
    for j in range(3):
        if cell != board[0][j] or board[0][j] == EMPTY:
            Horizontal = False
            break
    
    if Horizontal:
        return cell

    # Check second horizontal row
    cell = board[1][0]
    Horizontal = True
    for j in range(3):
        if cell != board[1][j] or board[1][j] == EMPTY:
            Horizontal = False
            break
    
    if Horizontal:
        return cell

    cell = board[2][0]
    Horizontal = True
    for j in range(3):
        if cell != board[2][j] or board[2][j] == EMPTY:
            Horizontal = False
            break
    
    if Horizontal:
        return cell

    
    cell = board[0][0]
    Vertical = True
    for i in range(3):
        if cell != board[i][0] or board[i][0] == EMPTY:
            Vertical = False
            break
    
    if Vertical:
        return cell

    cell = board[0][1]
    Vertical = True
    for i in range(3):
        if cell != board[i][1] or board[i][1] == EMPTY:
            Vertical = False
            break
    
    if Vertical:
        return cell

    
    cell = board[0][2]
    Vertical = True
    for i in range(3):
        if cell != board[i][2] or board[i][2] == EMPTY:
            Vertical = False
            break
    
    if Vertical:
        return cell

    cell = board[0][0]
    Diagonal = True
    for i in range(3):
        if cell != board[i][i] or board[i][i] == EMPTY:
            Diagonal = False
            break
    
    if Diagonal:
        return cell

    # Check right upwards diagonal
    cell = board[2][0]
    Diagonal = True

    if cell == EMPTY:
        Diagonal = False

    if cell != board[1][1] or board[1][1] == EMPTY:
        Diagonal = False

    if cell != board[0][2] or board[0][2] == EMPTY:
        Diagonal = False

    if Diagonal:
        return cell

    # No winner
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """

    checkIfWin = winner(board)
    if checkIfWin == X or checkIfWin == O:
        return True

    allCellsFilled = True

    for row in board:
        for cell in row:
            if cell == EMPTY:
                allCellsFilled = False

    if allCellsFilled:
        return True

    return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """

    checkIfWin = winner(board)

    if checkIfWin == X:
        return 1
    elif checkIfWin == O:
        return -1
    else:
        return 0
    

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """

    Player = player(board)

    allActions = actions(board)

    if Player == X:
        v = -2
        for act in allActions:
            minimumVal = minValue(result(board, act))
            if v < minimumVal:
                v = minimumVal
                bestAction = act
        return bestAction

    elif Player == O:
        v = 2
        for act in allActions:
            maximumVal = maxValue(result(board, act))
            if v > maximumVal:
                v = maximumVal
                bestAction = act
        return bestAction

    

def maxValue(board):
    if terminal(board):
        return utility(board)

    v = -2

    for act in actions(board):
        v = max(v, minValue(result(board, act)))
    
    return v


def minValue(board):
    if terminal(board):
        return utility(board)

    v = 2

    for act in actions(board):
        v = min(v, maxValue(result(board, act)))

    return v


def notValidAction(action):
    row, cell = action

    if row < 0 or row > 2:
        return True
    if cell < 0 or cell > 2:
        return True
    else:
        return False


def deepCopy(board):
    """
    Returns a deepcopy of the board
    """

    copy = []

    for i in range(3):
        row = []
        for j in range(3):
            row.append(board[i][j])
        copy.append(row)

    return copy
            

