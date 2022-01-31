from time import sleep

from .solver import *
from .entry_operations import (
    insert_value,
    delete_value,
    update_values, 
    collect_entry_values,
    update_values)

from src.gui.style.entry_color_change import (
    bg_to_red,
    bg_to_green,
    bg_to_blue,
    fg_to_blue,
    fg_to_white
)

IS_CLEAR = None
IS_VISUAL = None
HINT_BOARD = None
ENTRY_LIST = None
MASTER = None
RUN = True

select_time = 0.00
green_time = 0.05
red_time = 0.04

def stop_solving():
    global RUN
    RUN = False

def setup_visual_solve(master,entry_list, hint_board, is_clear, is_visual):
    global IS_CLEAR, IS_VISUAL, HINT_BOARD, ENTRY_LIST, MASTER, RUN

    IS_CLEAR = is_clear
    IS_VISUAL = is_visual
    HINT_BOARD = hint_board
    ENTRY_LIST = entry_list
    MASTER = master
    RUN = True


def speed_visual_solve(board):
    
    # if game not generated | input by user
    if not IS_VISUAL and IS_CLEAR:
        solve(board)
        update_values(board, ENTRY_LIST)
        return

    # Speed Solve | Game Generated
    if not IS_VISUAL:
        update_values(HINT_BOARD, ENTRY_LIST)

    # visual Solve
    if IS_VISUAL:
        find = find_empty(board)

        if not find:
            return True
        else:
            row, col = find

        for i in range(1,10):
            
            if IS_VISUAL and RUN:   # select
                bg_to_red(ENTRY_LIST[row][col])
                fg_to_white(ENTRY_LIST[row][col])
                delete_value(ENTRY_LIST[row][col])
                insert_value(ENTRY_LIST[row][col],i)
                MASTER.update()
                sleep(select_time)

            if valid(board, i, (row, col)):

                if IS_VISUAL and RUN:   # green / valid
                    bg_to_green(ENTRY_LIST[row][col])
                    delete_value(ENTRY_LIST[row][col])
                    insert_value(ENTRY_LIST[row][col],i)
                    MASTER.update()
                    sleep(green_time)
                
                board[row][col] = i

                if speed_visual_solve(board):
                    return True

                board[row][col] = 0

                if IS_VISUAL and RUN:
                    bg_to_red(ENTRY_LIST[row][col])
                    fg_to_white(ENTRY_LIST[row][col])
                    delete_value(ENTRY_LIST[row][col])
                    insert_value(ENTRY_LIST[row][col],0)
                    MASTER.update()
                    sleep(red_time)

        return False