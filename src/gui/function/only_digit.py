import re

def ONLY_DIGIT(e):
    if len(e) <= 2:
        if re.match(r"(\d).",e):
            return False
        if re.match(r"( (\d)|(\d)|(\d) )",e):
            return True
        elif e == " ":
            return True
        elif e == "":
            return True
        else:
            return False
    else: return False