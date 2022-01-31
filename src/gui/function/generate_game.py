import numpy as np
from random import sample
from .solver import *

# Game Possible : 362880

def gen_game(dif):

    # Create Empty Board 
    board = np.zeros((9,9), dtype=int)

    # Create Empty Hint Board
    hint_board = np.zeros((9,9), dtype=int)
    
    # Add random number to first row
    board[0] = sample(range(1,10), 9)

    # Solve the Board
    solve(board)

    # Board 2d to 1d
    # [9,9] -> [81]
    board = board.flatten()
    hint_board = hint_board.flatten()

    # remove values as per dificulty
    for i in sample(range(81),dif):
        hint_board[i] = board[i]
        board[i] = 0

    # reshape to [81] -> [9x9]
    board = np.reshape(board,(9,9))
    hint_board = np.reshape(hint_board,(9,9))
    
    # Add False where value 0
    disa_board = np.not_equal(board,0)

    return board, hint_board, disa_board
