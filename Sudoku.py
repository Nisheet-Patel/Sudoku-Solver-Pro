import tkinter as tk
from src.gui.sudoku_gui import GUI

'''
Sudoku Solver Pro
version: 0.1
Created By Nisheet Patel
Github: https://github.com/NisheetNakrani

- HElP -
# Run this command to install all dependencies/packages

pip3 install -r requirements.txt
or
pip install -r requirements.txt

'''

def main():
    root = tk.Tk()
    root.geometry("720x455")
    root.configure(background='white')
    root.title("Sudoku Pro")

    try:
        root.iconbitmap("icon\\sudoku.ico")
    except: pass

    Game = GUI(root)
    Game.generate_sudoku_board()
    Game.right_side_option_block()

    root.mainloop()

if __name__ == '__main__':
    main()