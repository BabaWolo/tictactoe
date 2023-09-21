"""
Tic Tac Toe Player
"""

import math
import copy

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
    # Initialize X and O count
    X_count = 0
    O_count = 0

    # Count number of X and O's played
    for sublist in board:
        for element in sublist:
            if element == X:
                X_count += 1
            elif element == O:
                O_count += 1
            else: continue

    # If equal amount of positions played, X's turn otherwise O's turn
    if X_count == O_count:
        player = X
        return player
    else:
        player = O
        return player


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """

    actions = set()

    # Add indices of playable actions
    for i, sublist in enumerate(board):
        for j, elements in enumerate(sublist):
            if elements != X and elements != O:
                actions.add((i, j))
    
    return actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    # Raise exception if action not valid
    if action not in actions(board):
        raise Exception("Your move is not valid")
    
    new_board_state = copy.deepcopy(board)
    new_board_state[action[0]][action[1]] = player(new_board_state)

    return new_board_state
    


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for row in board:
        if row[0]== row[1]== row[2]and row[0]!= EMPTY:
            return row[0]
        
    for colum in range(3):
        if board[0][colum] == board[1][colum] == board[2][colum] and board[0][colum] != EMPTY:
            return board[0][colum]
        
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != EMPTY:
        return board[0][0]
    
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != EMPTY:
        return board[0][2]
    
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    # Check if there's a winner
    if winner(board) == X or winner(board) == O:
        return True
    
    # Check for empty positions
    for row in board:
        for element in row:
            if element == EMPTY:
                return False
            
    # Game is a tie 
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    if winner(board) == O:
        return -1
    if winner(board) == None:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    # Initialize possible moves list
    moves = []

    # Find max or min valued move based on player
    if player(board) == X:
        # For every possible move add a utility value and the given action to the moves list
        for action in actions(board):
           moves.append([min_value(result(board, action)), action])
        # Sort the moves and return highest valued move
        moves.sort(key=lambda x: x[0], reverse=True)
        print(moves)
        return moves[0][1]
    else: 
        for action in actions(board):
        # For every possible move add a utility value and the given action to the moves list
            moves.append([max_value(result(board, action)), action])
        # Sort the moves and return lowest valued move
        moves.sort(key=lambda x: x[0])
        print(moves)
        return moves[0][1]
    
def max_value(board):
    if terminal(board):
        return utility(board)
    v = float("-inf")
    for action in actions(board):
        v = max(v, min_value(result(board, action)))
    return v

def min_value(board):
    if terminal(board):
        return utility(board)
    v = float("inf")
    for action in actions(board):
        v = min(v, max_value(result(board, action)))
    return v
