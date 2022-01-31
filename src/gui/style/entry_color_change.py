
'''
    define : change colors
    Use by : src\\gui\\function\\RCB_color_change.py
           : src\\gui\\function\\update_values.py
'''

# Colors
SELECT_COLOR = "#bbdefb"
HIGHLIGHT_COLOR = "#e2ebf3"
WHITE_COLOR = "white" 
BLACK_COLOR = "black"
FG_COLOR = "#2285e7"
RED_COLOR = "#d2372d"
LIGHTRED_COLOR = "#de6e67"
GREEN_COLOR = "#78db88"

#   ------------------- Blue --------------------    #


# Background to blue
#   user Select entry cell
def bg_to_blue(entry):
    entry.config(
        bg = SELECT_COLOR
    )

def readonly_bg_to_blue(entry):
    entry.config(
        readonlybackground = SELECT_COLOR
    )


#   -------------------- Lightblue -------------------    #


# Background to lightblue
#   color for highlight (row|colums|box) when user select entry cell
def bg_to_lightblue(entry):
    entry.config(
        bg = HIGHLIGHT_COLOR
    )

def readonly_bg_to_lightblue(entry):
    entry.config(
        readonlybackground = HIGHLIGHT_COLOR
    )


#   -------------------- White ------------------    #


# Background to White
#   set to default color
def bg_to_white(entry):
    entry.config(
        bg = WHITE_COLOR
    )

def readonly_to_white(entry):
    entry.config(
        readonlybackground = WHITE_COLOR
    )


#   -------------------- Red ------------------    #

def bg_to_red(entry):
    entry.config(
        bg = LIGHTRED_COLOR
    )


#   -------------------- Green ------------------    #

def bg_to_green(entry):
    entry.config(
        bg = GREEN_COLOR
    )


#   -------------------- Font Color ------------------    #


# Blue
def fg_to_blue(entry):
    entry.config(
        fg = FG_COLOR
    )

# Black
def reset_fg_to_black(entry):
    entry.config(
        fg = BLACK_COLOR
    )

# Red
def fg_to_red(entry):
    entry.config(
        fg = RED_COLOR
    )

# White
def fg_to_white(entry):
    entry.config(
        fg = WHITE_COLOR
    )


#   -------------------- Board Color Chnage ------------------    #

def board_fg_to_blue(entry_list, board):
    for i in range(9):
        for j in range(9):
            # try:
            bg_to_white(entry_list[i][j])
            if board[i][j] == 0:
                fg_to_blue(entry_list[i][j])
            # except:
            readonly_to_white(entry_list[i][j])