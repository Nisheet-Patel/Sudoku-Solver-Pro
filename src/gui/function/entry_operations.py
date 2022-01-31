import re
import numpy as np
from src.gui.style.entry_color_change import (
    bg_to_white,
    readonly_to_white,
    fg_to_blue,
    reset_fg_to_black
)

# entry to read only mode
def read_only_mode(entry):
    entry.config(
        state='readonly',
        readonlybackground='white'
    )

# entry to normal mode
def normal_mode(entry):
    entry.config(
        state='normal'
    )


# delete value from entry
def delete_value(entry):
    entry.delete(0, 'end')

# insert value in entry
def insert_value(entry,n):
    entry.insert(0," {}".format(n))

# format value "5" -> " 5" 
def format_value(entry):
    VALUE = entry.get()

    if re.match(r"(\d)",VALUE):
        delete_value(entry)
        insert_value(entry,VALUE)



# insert values in gui with readonly mode
def update_board(board,entry_list):
    for i in range(9):
        for j in range(9):
            entry = entry_list[i][j]

            normal_mode(entry)
            
            delete_value(entry)

            # readonly mode
            if board[i][j] > 0:
                insert_value(entry,board[i][j])
                read_only_mode(entry)
                readonly_to_white(entry)
                reset_fg_to_black(entry)
            else:
                fg_to_blue(entry)
                bg_to_white(entry)



# write values in gui of hint_board
#   Speed solve
def update_values(hint_board,entry_list):
    for i in range(9):
        for j in range(9):
            entry = entry_list[i][j]

            # not in readonly mode
            if hint_board[i][j] > 0:
                delete_value(entry)
                insert_value(entry,hint_board[i][j])
                fg_to_blue(entry)
                bg_to_white(entry)



# delete all values from gui
# not disabled ones 
def restart_board(board,entry_list):

    for i in range(9):
        for j in range(9):

            if board is None:
                 delete_value(entry_list[i][j])
            elif board[i][j] == 0:
                delete_value(entry_list[i][j])


# Clear all values from gui
# with disabled ones
def clear_all_board(board,entry_list):
    for i in range(9):
        for j in range(9):
            entry = entry_list[i][j]

            if board is not None:
                if board[i][j] > 0:
                    normal_mode(entry)

            delete_value(entry)
            fg_to_blue(entry)
            bg_to_white(entry)


# collect entry values from gui
#   for speed_visual_solve
def collect_entry_values(entry_list):

    board = np.zeros((9,9), dtype=int)

    for i in range(9):
        for j in range(9):
            format_value(entry_list[i][j])
            VALUE = entry_list[i][j].get()
            try:
                board[i][j] = int(VALUE)
            except: pass
    return board
