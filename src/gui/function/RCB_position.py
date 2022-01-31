
'''
    { R : Row, C : Column, B : Box }
    calculate and return rows, columns & box indexs with given index
    
    return : 2d List
    Use by : src\\gui\\function\\RCB_color_change.py
'''


def get_RCB_pos(x,y) -> set:
    pos = set()

    # Add row indexs
    for i in range(9):
        pos.add((x,i))

    # Add columns indexs
    for i in range(9):
        pos.add((i,y))

    # Add box indexs
    box_x = x // 3
    box_y = y // 3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x * 3, box_x*3 + 3):
            pos.add((j,i))
        
    return pos
    