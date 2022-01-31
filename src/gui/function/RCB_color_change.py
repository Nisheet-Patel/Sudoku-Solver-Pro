from src.gui.style.entry_color_change import *
from .RCB_position import *

'''
    { R : Row, C : Column, B : Box }

    Change color of Row, Column, and Box
    Use by : src\\gui\\sudoku_gui.py
'''

# Highlight RCB as per current selection
def change_RCB_color(entry_list,readonly_board,x,y):
    # POS - all RCB indexs
    _POS = get_RCB_pos(x,y)

    for i in range(len(_POS)):
        POS = _POS.pop()

        if readonly_board[POS[0]][POS[1]]:
            readonly_bg_to_lightblue(entry_list[POS[0]][POS[1]])
        else:
            bg_to_lightblue(entry_list[POS[0]][POS[1]])
    
    # change current selected color
    if readonly_board[x][y]:
        readonly_bg_to_blue(entry_list[x][y])
    else:
        bg_to_blue(entry_list[x][y]) 



# Remove Highlight color of RCB of previous selection
def reset_RCB_color(entry_list,readonly_board,x,y):
    # POS - all RCB indexs
    _POS = get_RCB_pos(x,y)

    for i in range(len(_POS)):
        POS = _POS.pop()

        if readonly_board[POS[0]][POS[1]]:
            readonly_to_white(entry_list[POS[0]][POS[1]])
        else:
            bg_to_white(entry_list[POS[0]][POS[1]])