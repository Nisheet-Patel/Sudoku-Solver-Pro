import tkinter as tk
import numpy as np

from .style._style import STYLE
from .style.entry_color_change import board_fg_to_blue

from .function.only_digit import ONLY_DIGIT
from .function.RCB_color_change import *
from .function.generate_game import gen_game
from .function.entry_operations import (
    update_board, 
    format_value,
    insert_value,
    delete_value, 
    restart_board, 
    clear_all_board,
    collect_entry_values)
from .function.valid_entry_color_change import is_valid
from .function.speed_visual_solve import *

from .bot.autotype import BOT

class GUI(STYLE):
    def __init__(self, _master):
        super().__init__()

        # root Window
        self._master = _master
        
        # Game Board Entry boxes
        self.Entry_list = [[" " for i in range(9)] for j in range(9)]

        # Game Boards
        self.Game_board = None
        self.Readonly_board = np.zeros((9,9), dtype=int)
        self.Hint_board = None

        # Entry Queue
        self.Entry_Queue = []

        # Current Selected Position by User
        self.c_pos_x = None
        self.c_pos_y = None
        
        # Permission
        self.is_clear = True
        self.visual_running = False

        # Register new Function
        self.only_digit = self._master.register(ONLY_DIGIT)

        # Is Running 
        self.running = False

    # bind function with input boxes to update current position
    
    def start_running(self):
        self.running = True
    
    def stop_running(self):
        self.running = False
    
    def update_current_position(self, x, y):
        self.c_pos_x = x
        self.c_pos_y = y

    # Generate 81 input boxes with space between them after 3
    # Frame at 0,0
    def generate_sudoku_board(self):
        Board_frame = tk.Frame(self._master)
        Board_frame.grid(row=0, column=0, pady=2)

        p = 0
        for i in range(9):
            q = 0
            for j in range(9):
                # Space Between rows
                if (p+1) % 4 == 0 and p != 0:
                    l1 = tk.Canvas(Board_frame,width=1,height=1,bg="white")
                    l1.grid(row=p, column=q)
                    p += 1
                # Space Between columns
                if (q+1) % 4 == 0 and q != 0:
                    l1 = tk.Canvas(Board_frame,width=1,height=1,bg="white")
                    l1.grid(row=p, column=q)
                    q += 1

                # Create Entry Boxes
                entry = tk.Entry(
                    Board_frame,
                    width=2,
                    font=("Helvetica", 30),
                    bg="white",
                    relief="ridge",
                    validate ="key",
                    validatecommand = (self.only_digit, '%P'))

                entry.grid(row=p, column=q)
                
                # bind funtion to update (c_pos_x, c_pos_y) when user select any box  
                entry.bind("<Button-1>", lambda e=None, x=i, y=j: self.entry_on_left_click(x, y))
                entry.bind("<Button-3>", lambda e=None, x=i, y=j: self.entry_on_right_click(x, y))
                
                
                entry.insert(0, " ")
                q += 1
                self.Entry_list[i][j] = entry
            p += 1

    # Frame At 0,1
    def right_side_option_block(self):

        # {1} Main Right side frame
        right_block_frame = tk.Frame(self._master,bg="white")
        

        # {1-1} Title Frame = [ "SUDOKU" ]
        # +------------------------------+
        # |           SUDOKU             |
        # +------------------------------+
        title_frame = tk.Frame(right_block_frame,bg="white")
        
        # "SUDOKU" Title 
        title = tk.Label(title_frame, 
            text="SUDOKU", 
            fg = self.Option_title["fg"],
            bg = self.Option_title["bg"],
            font = self.Option_title["font"]
            )
        title.grid(row=0,column=0)

        title_frame.grid(row=0,column=0)
        ## {1-1}

        # {1-2}  All Button option [ New Game, Clear, Help, Solve ]
        option_frame = tk.Frame(right_block_frame,bg="white")
        

        # {1-2-1} New Game LabelFrame = [ Easy, Hard ]
        # +------------------------------+
        # |          NEW Game            |
        # +------------------------------+
        new_game_label_frame = tk.LabelFrame(option_frame,text="  NEW GAME ")
        self.Option_Frame_Add_Style(new_game_label_frame)

        easy_game = tk.Button(new_game_label_frame, text = "Easy", command= lambda : self.easy_hard_game_button_action(41))
        self.Option_Button_Add_Style(easy_game)
        easy_game.grid(row=0,column=0, padx=self.Option_Button_padx, pady=self.Option_Button_pady)

        hard_game = tk.Button(new_game_label_frame, text = "Hard", command= lambda : self.easy_hard_game_button_action(56))
        self.Option_Button_Add_Style(hard_game)
        hard_game.grid(row=0,column=1, padx=self.Option_Button_padx, pady=self.Option_Button_pady)
        
        new_game_label_frame.grid(row=0, column=0, pady=self.Option_Frame_pady)
        ## {1-2-1}


        # {1-2-2} Clear LabelFrame = [ Restart, Clear All ]
        # +------------------------------+
        # |            CLEAR             |
        # +------------------------------+
        clear_label_frame = tk.LabelFrame(option_frame, text="  CLEAR  ")
        self.Option_Frame_Add_Style(clear_label_frame)

        restart_game = tk.Button(clear_label_frame, text="Restart", command=self.restart_button_action)
        self.Option_Button_Add_Style(restart_game)
        restart_game.grid(row=0,column=0, padx=self.Option_Button_padx, pady=self.Option_Button_pady)

        clear_all_game = tk.Button(clear_label_frame, text = "Clear All", command=self.clear_all_button_action)
        self.Option_Button_Add_Style(clear_all_game)
        clear_all_game.grid(row=0,column=1, padx=self.Option_Button_padx, pady=self.Option_Button_pady)

        clear_label_frame.grid(row=1, column=0, pady=self.Option_Frame_pady)
        ## {1-2-2}
        

        # {1-2-3} Help LabelFrame = [ Hint, Bot ]
        # +------------------------------+
        # |             HELP             |
        # +------------------------------+
        help_label_frame = tk.LabelFrame(option_frame, text="  HELP  ")
        self.Option_Frame_Add_Style(help_label_frame)

        hint_b = tk.Button(help_label_frame, text="Hint", command=self.hint_button_action)
        self.Option_Button_Add_Style(hint_b)
        hint_b.grid(row=0,column=0, padx=self.Option_Button_padx, pady=self.Option_Button_pady)

        self.bot_b = tk.Button(help_label_frame, text = "Bot", command=self.bot_button_action)
        self.Option_Button_Add_Style(self.bot_b)
        self.bot_b.grid(row=0,column=1, padx=self.Option_Button_padx, pady=self.Option_Button_pady)

        help_label_frame.grid(row=2, column=0, pady=self.Option_Frame_pady)
        ## {1-2-3}


        # {1-2-3} Solve LabelFrame = [ visual, Speed ]
        # +------------------------------+
        # |            SOLVE             |
        # +------------------------------+
        solve_label_frame = tk.LabelFrame(option_frame, text="  SOLVE  ")
        self.Option_Frame_Add_Style(solve_label_frame)

        visual_game = tk.Button(solve_label_frame, text="Visual", command=lambda : self.speed_visual_solve_button_action(True))
        self.Option_Button_Add_Style(visual_game)
        visual_game.grid(row=0,column=0, padx=self.Option_Button_padx, pady=self.Option_Button_pady)

        speed_game = tk.Button(solve_label_frame, text = "Speed", command=lambda : self.speed_visual_solve_button_action(False))
        self.Option_Button_Add_Style(speed_game)
        speed_game.grid(row=0,column=1, padx=self.Option_Button_padx, pady=self.Option_Button_pady)

        solve_label_frame.grid(row=3, column=0, pady=self.Option_Frame_pady)
        ## {1-2-3}

        option_frame.grid(row=1, column=0)
        ## {1-2}
        
        right_block_frame.grid(row=0, column=1, padx=10)     
        ## {1}
        
    # +------------------------------+
    # |      Left Click Action       |
    # +------------------------------+
    # Actions when entry box selected
    def entry_on_left_click(self,x,y):
        if not self.visual_running:
            # Add to entry_queue
            self.add_to_entry_queue(x,y)

            # update current position
            self.update_current_position(x, y)
            
            # remove highlight color from previously selected cell
            if len(self.Entry_Queue) == 2:
                entry = self.Entry_list[self.Entry_Queue[0][0]][self.Entry_Queue[0][1]]

                format_value(entry)

                # Remove Highlight of RCB Color
                reset_RCB_color(self.Entry_list,self.Readonly_board,self.Entry_Queue[0][0],self.Entry_Queue[0][1])
                
                # if value(answer) is wrong then change color to red
                if self.Hint_board is not None:
                    is_valid(entry, self.Hint_board[self.Entry_Queue[0][0]][self.Entry_Queue[0][1]])

            # Highlight RCB Color
            change_RCB_color(self.Entry_list,self.Readonly_board,x,y)

    # +------------------------------+
    # |     Right Click Action       |
    # +------------------------------+
    def entry_on_right_click(self,x,y):
        # remove value of current cell
        delete_value(self.Entry_list[x][y])

    # +----------------------------------+
    # |      Easy, Hard Game Action      |
    # +----------------------------------+
    def easy_hard_game_button_action(self,dif):
        if not self.running:
            # update boards : Game_board, Hint_board, Readonly_board
            self.Game_board,self.Hint_board,self.Readonly_board = gen_game(dif)

            # insert values in gui
            update_board(self.Game_board, self.Entry_list)

            self.is_clear = False

            # clear Queue
            self.Entry_Queue.clear()

    # +------------------------------+
    # |        Restart Action        |
    # +------------------------------+
    def restart_button_action(self):
        # Stop Visual Solving
        stop_solving()

        # Just remove user input values not readonly ones
        restart_board(self.Game_board,self.Entry_list)

    # +--------------------------------+
    # |        Clear All Action        |
    # +--------------------------------+
    def clear_all_button_action(self):
        # Stop Visual Solving
        stop_solving()

        # clear all game 
        clear_all_board(self.Game_board,self.Entry_list)

        # reset all boards fill with 0
        self.Game_board = None
        self.Readonly_board = np.zeros((9,9), dtype=int)
        self.Hint_board = None

        self.is_clear = True
        self.Entry_Queue.clear()

    # +------------------------------+
    # |         Hint Action          |
    # +------------------------------+
    def hint_button_action(self):
        # if board is clear it didn't insert hint value
        if not self.is_clear:
            insert_value(self.Entry_list[self.c_pos_x][self.c_pos_y],self.Hint_board[self.c_pos_x][self.c_pos_y])
            
    
    # +---------------------------------------------+
    # |         Speed & Visual Solve Action         |
    # +---------------------------------------------+
    def speed_visual_solve_button_action(self, is_visual):
        # if visual call and virual solve already running then it return
        if is_visual and self.running:
            return

        # running -> True | if visual call
        if is_visual:
            self.start_running()

        self.visual_running = True

        # Game Not Generate collect values from input box
        if self.is_clear:
            board = collect_entry_values(self.Entry_list)
            self.Game_board = board.copy()
        else:
            # copy current generated board
            board = self.Game_board.copy()

        b = board.copy()

        # setup environment 
        setup_visual_solve(self._master, self.Entry_list, self.Hint_board, self.is_clear, is_visual)

        # Solving 
        speed_visual_solve(board)

        # visual call then current selected cell to blue
        if is_visual:
            board_fg_to_blue(self.Entry_list,b)

        # delete temp boards
        del b,board

        self.visual_running = False

        # running -> False | if visual call
        if is_visual:
            self.stop_running()

    # +------------------------------+
    # |         Bot Action           |
    # +------------------------------+
    def bot_button_action(self):
        bot =  BOT()
        if not self.is_clear:
            pass
        if not self.running:
            self.start_running()
            self.bot_b.config(text="Stop")
            bot.auto_type(self.Game_board,self.Entry_list, self._master)
            self.bot_b.config(text="Bot")
            self.stop_running()
        else:
            bot.stop_bot()
            self.stop_running()
            self.bot_b.config(text="Bot")
            board_fg_to_blue(self.Entry_list, self.Game_board)


    # return current selected position
    def get_c_pos(self):
        return self.c_pos_x, self.c_pos_y

    # FILO to store last clicked entry
    def add_to_entry_queue(self,x,y):
        if len(self.Entry_Queue) == 2:
            self.Entry_Queue.pop(0)
        self.Entry_Queue.append([x,y])