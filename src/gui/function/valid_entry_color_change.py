from src.gui.style.entry_color_change import fg_to_red, fg_to_blue

'''
    - Change font color to red 
        if answer/value is wrong
        else font color to blue
        
    use by : sudoku_gui.py
'''

def is_valid(entry,hint_board_val):
    if int(hint_board_val) != 0:
        VALUE = entry.get()
        if VALUE != "":
            if int(VALUE) != int(hint_board_val):
                fg_to_red(entry)
            if int(VALUE) == int(hint_board_val):
                fg_to_blue(entry)