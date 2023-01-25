# Student name: Minhui Roh
# McGill ID: 261120462

MOVEMENT_SYMBOLS = "><v^"
EMPTY_SYMBOL = "."
TREASURE_SYMBOL = "+"
BREADCRUMB_SYMBOL = "X"
MOVEMENT_SYMBOLS_3D = "*|"

def get_nth_row_from_map(map_string, n, width, height):
    """ (str, int, int, int) -> str
    Takes the map string, row number n, map width and height as inputs.
    Returns a string corresponding to the specified row.
    If n is not valid, returns an empty string. 
    
    >>> get_nth_row_from_map("^..>>>..v", 1, 3, 3)
    '>>>'
    >>> get_nth_row_from_map("v..v.v.<", 0, 4, 2)
    'v..v'
    >>> get_nth_row_from_map("......", 3, 2, 3)
    ''
    """
    start_point = n * width
    end_point = ((n+1) * width)
    if n >= height or n < 0:
        return ""
    return map_string[start_point:end_point]

def print_treasure_map(map_string, width, height):
    """ (str, int, int) -> NoneType
    Takes the map string, width and height as inputs.
    Returns nothing but prints out the treasure map according to width and height values.
    
    >>> print_treasure_map("<..vvv..^", 3, 3)
    <..
    vvv
    ..^
    >>> print_treasure_map("v..v.v.<", 4, 2)
    v..v
    .v.<
    >>> print_treasure_map(">.vv<..>><<v", 3, 4)
    >.v
    v<.
    .>>
    <<v
    """
    row = 0
    while row < height:
        print (get_nth_row_from_map (map_string, row, width, height))
        row += 1

def change_char_in_map(map_string, row, column, c, width, height):
    """ (str, int, int, str, int, int) -> str
    Takes the map string, row and column number, c which is a replacing string, width and height of the map
    as inputs. Returns the string with characters replaced by c at designated row/column coordinate.
    Returns the map string itself if row and column is not contained in the map.
    
    >>> change_char_in_map (".........", 1, 1, "X", 3, 3)
    '....X....'
    >>> change_char_in_map ("<.>.<.>.", 2, 1, "B", 2, 4)
    '<.>.<B>.'
    >>> change_char_in_map (".........", 3, 1, "X", 3, 3)
    '.........'
    """
    front_segment = map_string [0: width*row + column]
    back_segment = map_string [width*row + column + 1:]
    if row >= height or column >= width or row < 0 or column < 0:
        return map_string
    return front_segment + c + back_segment

def get_proportion_travelled(map_string):
    """ (str) -> float
    Takes a map string as an input and returns a float rounded to two decimal places indicating
    the percentage of breadcrumb symbols on the map.
    
    >>> get_proportion_travelled (".X..X.XX.")
    0.44
    >>> get_proportion_travelled ("X.X.X.")
    0.5
    >>> get_proportion_travelled ("......")
    0.0
    >>> get_proportion_travelled (".X.")
    0.33
    """
    
    return round (map_string.count(BREADCRUMB_SYMBOL) / len(map_string), 2)

def get_nth_map_from_3D_map(map_string, n, width, height, depth):
    """ (str, int, int, int, int) -> str
    Takes a map string, map number, and map width, height, and depth as inputs.
    Returns a string corresponding to the right map number.
    
    >>> get_nth_map_from_3D_map(".X.XXX.X..v.vXv.v.", 0, 3, 3, 2)
    '.X.XXX.X.'
    >>> get_nth_map_from_3D_map(".v>v>^Xv.^v^", 1, 3, 2, 2)
    'Xv.^v^
    >>> get_nth_map_from_3D_map("^^..vv", 2, 2, 1, 3)
    'vv'
    """
    if n >= depth or n < 0:
        return ""
    start_point = n * width * height
    end_point = (n+1) * width * height
    return map_string[start_point : end_point]

def print_3D_treasure_map(map_string, width, height, depth):
    """ (str, int, int, int) -> NoneType
    Takes a map string and integer width, height, and depth as inputs.
    Returns nothing but prints out the 3D treasure map according to its size.
    
    >>> print_3D_treasure_map(".X.XXX.X..v.vXv.v.", 3, 3, 2)
    .X.
    XXX
    .X.
    
    .v.
    vXv
    .v.
    >>> print_3D_treasure_map(".v..^.v.v^.^", 3, 2, 2)
    .v.
    .^.
    
    v.v
    ^.^
    >>> print_3D_treasure_map("X.X.^.<.>", 3, 1, 3)
    X.X
    
    .^.
    
    <.>
    """
    for i in range (depth):
        nth_map = get_nth_map_from_3D_map(map_string, i, width, height, depth)
        print_treasure_map(nth_map, width, height)
        if i == depth - 1:
            break
        print("")

def change_char_in_3D_map(map_string, row, column, depth_index, c, width, height, depth):
    """ (str,int,int,int,str,int,int,int) -> str
    Takes a map string, row, column, depth indexes, replacing character c, width, height, depth values
    as inputs. Returns the copy of the map string with a character being replaced at specific coordinates.
    
    >>> change_char_in_3D_map(".X.XXX.X..v.vXv.v.", 0, 0, 0, "#", 3, 3, 2)
    '#X.XXX.X..v.vXv.v.'
    >>> change_char_in_3D_map(".v..^.v.v^.^", 0, 2, 1, "X", 3, 2, 2)
    '.v..^.v.X^.^'
    >>> change_char_in_3D_map("X.X.^.<.>", 0, 1, 1, "B", 3, 1, 3)
    'X.X.B.<.>'
    >>> change_char_in_3D_map(".X.XXX.X..v.vXv.v.", 0, 0, 2, "#", 3, 3, 2)
    '.X.XXX.X..v.vXv.v.'
    """
    if row >= height or row < 0 or column >= width or column < 0 or depth_index >= depth or depth_index < 0:
        return map_string
    front_segment = map_string[0:width*height*depth_index + width*row + column]
    back_segment = map_string[width*height*depth_index + width*row + column + 1:]
    return front_segment + c + back_segment
        

    


    













        