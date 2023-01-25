# Student name: Minhui Roh
# McGill ID: 261120462

import random
from treasure_utils import *

def generate_treasure_map_row(width, boolean):
    """ (int,bool) -> str
    Takes a positive integer width and a boolean indicating whether the map is being generated as inputs
    or not. Returns a row of string with given width. A character has 5/6 chance to be movement symbol and
    1/6 chance to be an empty symbol.
    
    >>> random.seed(9001)
    >>> generate_treasure_map_row(10, False)
    '<^<<<<<.vv'
    >>> random.seed(9001)
    >>> generate_treasure_map_row(10, True)
    '<|<<<<<.vv'
    >>> random.seed(8001)
    >>> generate_treasure_map_row(15, True)
    '^..v^^v.v.^.^.v'
    >>> random.seed(5001)
    >>> generate_treasure_map_row(10, True)
    '<v<^*><^>^'
    """
    row_str=""
    for i in range(width):
        random_int = random.randint(1, 120)
        if random_int >= 101:
            row_str += EMPTY_SYMBOL
        else:
            row_str += MOVEMENT_SYMBOLS[random_int % 4]
    if boolean == True:
        random_int = random.randint(0, 2*width - 1)
        if random_int < width:
            c = MOVEMENT_SYMBOLS_3D [random_int % 2]
            row_str = change_char_in_map(row_str, 0, random_int, c, width, 1)
    return row_str

def generate_treasure_map(width, height, boolean):
    """ (int,int,bool) -> str
    Takes integers width and height and a boolean as inputs.
    Generates a treasure map of given size and return it as a string.
    
    >>> random.seed(9001)
    >>> generate_treasure_map(3, 3, False)
    '>^<<<<<.v'
    >>> random.seed(9001)
    >>> generate_treasure_map(5, 6, True)
    '>^<<*<.vv*^<<vvv.>vv<v^<v^.^|.'
    >>> random.seed(8001)
    >>> generate_treasure_map(4, 5, True)
    '>..vv.v..vv>*>v>v^<>'
    """
    treasure_map = ""
    for i in range (height):
        treasure_map += generate_treasure_map_row(width, boolean)
    return change_char_in_map(treasure_map, 0, 0, MOVEMENT_SYMBOLS[0], width, height)

def generate_3D_treasure_map(width, height, depth):
    """ (int,int,int) -> str
    Takes a positive integer width, height and depth as inputs.
    Returns a 3D treasure map of the given measurements as string.
    
    >>> random.seed(9001)
    >>> generate_3D_treasure_map(3, 3, 3)
    '>^<<<<v^>>^^<v*v.>>v<^<v^|^'
    >>> random.seed(9001)
    >>> generate_3D_treasure_map(2, 2, 2)
    '>^<<>.><'
    >>> random.seed(9001)
    >>> generate_3D_treasure_map(4, 4, 4)
    '>^<<*.vv><.^v|>v><v|v^^...<>.<*<>v<>^|>.*^v.*.><>^<<v|^<<>.|^^^v'
    """
    treasure_map_3D = ""
    for i in range (depth):
        treasure_map_3D += generate_treasure_map(width, height, True)
    return change_char_in_3D_map(treasure_map_3D, 0, 0, 0, MOVEMENT_SYMBOLS[0], width, height, depth)

def follow_trail(map_string, row, column, depth_index, width, height, depth, n_tiles):
    """ (str,int,int,int,int,int,int,int) -> str
    Takes 3D treasure map string, starting row, column, depth index as well as width, height and depth
    of the map and number of tiles to travel as inputs.
    Follows the trail until specified tile number has been met or crossing same path twice.
    Prints the number of collected treasures and the number of symbols visited.
    Returns the travelled map.
    
    >>> follow_trail(">+....",0,0,0,3,2,1,3)
    Treasures collected: 1
    Symbols visited: 3
    'X+....'
    >>> follow_trail(">+v..*<.<.+<", 0,0,0,3,2,2,20)
    Treasures collected: 2
    Symbols visited: 7
    'X+X..X<.<.+X'
    >>> follow_trail(".v.*v<*^..>|", 0,1,0,2,2,3,100)
    Treasures collected: 0
    Symbols visited: 8
    '.X.XXXXX..XX
    >>> follow_trail(">.v.|*>^v.v.<^*|..^^^.|<...", 2,0,1,3,3,3,6)
    Treasures collected: 0
    Symbols visited: 6
    '>.v.X*XXv.v.<X*X..^^^.X<...'
    """
    if row >= height or row < 0 or column >=width or column < 0 or depth_index >= depth or depth_index < 0:
        return map_string
    start_index = depth_index * width * height + row * width + column
    start_symbol = map_string[start_index]
    symbol = start_symbol
    tiles_travelled = 0
    treasures_collected = 0
    previous_symbol = start_symbol
    t_map=map_string
    #t_map for travelled_map
    while symbol != BREADCRUMB_SYMBOL and tiles_travelled != n_tiles:
        if symbol == EMPTY_SYMBOL:
            symbol = previous_symbol
        elif symbol == TREASURE_SYMBOL:
            symbol = previous_symbol
            treasures_collected += 1
        else:    
            previous_symbol = map_string[depth_index * width * height + row * width + column]
            t_map=change_char_in_3D_map(t_map,row,column,depth_index,BREADCRUMB_SYMBOL,width,height,depth)
        tiles_travelled += 1
        if symbol == MOVEMENT_SYMBOLS[0]:
            if column == width - 1:
                column = 0
            else:
                column += 1
        elif symbol == MOVEMENT_SYMBOLS[1]:
            if column == 0:
                column += width - 1
            else:
                column -= 1
        elif symbol == MOVEMENT_SYMBOLS[2]:
            if row == height - 1:
                row = 0
            else:
                row += 1
        elif symbol == MOVEMENT_SYMBOLS[3]:
            if row == 0:
                row += height - 1
            else:
                row -= 1
        elif symbol == MOVEMENT_SYMBOLS_3D[0]:
            if depth_index == depth - 1:
                depth_index = 0
            else:
                depth_index += 1
        elif symbol == MOVEMENT_SYMBOLS_3D[1]:
            if depth_index == 0:
                depth_index = depth - 1
            else:
                depth_index -= 1

        index = depth_index * width * height + row * width + column
        symbol = t_map[index]
    print ("Treasures collected: "+ str(treasures_collected))
    print ("Symbols visited: " + str(tiles_travelled))
    return t_map

        
        
            
            

    


















