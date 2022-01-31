from tkinter import messagebox
import pyautogui
from time import sleep

from src.gui.style.entry_color_change import (
    board_fg_to_blue,
    bg_to_green,
    board_fg_to_blue
)

class BOT:
    bot_running = False
    def __init__(self):
        self.bot_sleep = 0

    def stop_bot(self):
        BOT.bot_running = False 

    def auto_type(self, board, entry_list, master):

        self.message = '''
        Bot will Start in 5 seconds 
        so press ok and click on first cell
        of game on website or any other platform.

        Note: This will press Number keys as per sudoku board 

        * Click on top left first cell
        '''

        if not BOT.bot_running:
            self.user_messagebox = messagebox.askokcancel(title="Read it First", message=self.message)
            
            if self.user_messagebox:
                board_fg_to_blue(entry_list, board)
                master.update()
                BOT.bot_running = True

                sleep(5)
                for i in range(9):
                    for j in range(9):
                        if BOT.bot_running == False:
                            return

                        if (i+1)%2==0:
                            pyautogui.press(str(entry_list[i][8-j].get()).strip())
                            pyautogui.press('left')
                            bg_to_green(entry_list[i][8-j])
                            master.update()
                        else:
                            pyautogui.press(str(entry_list[i][j].get()).strip())
                            pyautogui.press('right')
                            bg_to_green(entry_list[i][j])
                            master.update()
                        sleep(self.bot_sleep)
                    pyautogui.press('down')

            BOT.bot_running = False
