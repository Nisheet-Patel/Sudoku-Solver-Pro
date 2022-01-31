import json

class Option_Style:
    def __init__(self):
        '''
            Loads : "Option_block_style.json" 
            Use by : _style.py
        '''

        file = open("src\\gui\\style\\Option_block_style.json",'r')
        data = json.load(file)
        
        self.Option_Frame = data["Option_Frame"]
        self.Option_Button = data["Option_Button"]
        
        # Main Screen Style
        self.Main_bg = data["Main"]

        # Main SUDOKU Title Style
        self.Option_title = data["Title"]

        # Button Style Variables
        self.Option_Button_padx = self.Option_Button["padx"]
        self.Option_Button_pady = self.Option_Button["pady"]

        # LabelFrame Style Variables 
        self.Option_Frame_pady = self.Option_Frame["pady"]

        file.close()
