# Load data

import sys

is_test = False
if len(sys.argv) > 1 and sys.argv[1] == "t":
    is_test = True
    load_file = "input.txt"
elif len(sys.argv) > 1:
    sample_name = sys.argv[1]
    load_file = "sample_" + sample_name + ".txt"
else:
    load_file = "sample.txt"

print(f"{is_test=}", load_file)

with open(load_file) as f:
    data =  f.readlines()
        
data = [l.strip() for l in data]

def print_matrix(matrix):
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            print(matrix[row][col], end="")
        print()

# Problem solution
# Handle input data
dataset_splitter = data.index('')
field_lines = data[:dataset_splitter]
move_lines = data[dataset_splitter+1:]

moves = list("".join(move_lines))
if not is_test:
    print("Moves:")
    print(moves)

ORIGINAL_SIZE = len(field_lines)
ROWS = ORIGINAL_SIZE
COLUMNS = 2 * ROWS

original_field = [list(s) for s in field_lines]
if not is_test:
    print("Field:")
    print_matrix(original_field)

# Set up constants
EMPTY = "."
WALL = "#"
BOX = "O"
BOX_LEFT = "["
BOX_RIGHT = "]"
ROBOT = "@"

NORTH = "^"
EAST = ">"
SOUTH = "v"
WEST = "<"

directions = {
    NORTH : (-1, 0),
    EAST : (0, 1),
    SOUTH : (1, 0),
    WEST : (0, -1)
}
cur_row, cur_col = None, None
field = [['-' for _ in range(COLUMNS)] for _ in range(ROWS)]

for r in range(ORIGINAL_SIZE):
    for c in range(ORIGINAL_SIZE):
        if original_field[r][c] == EMPTY:
            field[r][c*2] = EMPTY
            field[r][c*2+1] = EMPTY

        if original_field[r][c] == WALL:
            field[r][c*2] = WALL
            field[r][c*2+1] = WALL

        if original_field[r][c] == BOX:
            field[r][c*2] = BOX_LEFT
            field[r][c*2+1] = BOX_RIGHT

        if original_field[r][c] == ROBOT:
            field[r][c*2] = ROBOT
            field[r][c*2+1] = EMPTY
            cur_row = r
            cur_col = c*2

print_matrix(field)

assert cur_row is not None
assert cur_col is not None           

def move_item(from_r, from_c, to_r, to_c):
    field[to_r][to_c] = field[from_r][from_c]
    field[from_r][from_c] = EMPTY

def move(r: int, c: int, direction: str, act: bool):
    dr, dc = directions[direction]

    if field[r+dr][c+dc] == WALL:
        return False

    if field[r+dr][c+dc] == EMPTY:
        if act:
            move_item(r,c,r+dr,c+dc)
        return True
    
    if field[r+dr][c+dc] == ROBOT:
        raise Exception("Something is wrong. Found robot")
    
    # Must be box hereon from
    if direction == NORTH or direction == SOUTH:
        
        if field[r+dr][c+dc] == BOX_LEFT:
            box_left = (r+dr, c+dc)
            box_right = (r+dr, c+dc+1)
        elif field[r+dr][c+dc] == BOX_RIGHT:
            box_left = (r+dr, c+dc-1)
            box_right = (r+dr, c+dc)
        else:
            raise Exception("What box?")

        left_can_move = move(*box_left, direction, act=False)
        right_can_move = move(*box_right, direction, act=False)

        if not (left_can_move and right_can_move):
            return False
        
        move(*box_left, direction, act=act)
        move(*box_right, direction, act=act)

        if act:
            # Move current
            move_item(r,c,r+dr,c+dc)

            # If current is left side of box, move right side aswell
            if field[r][c] == BOX_LEFT:
                move_item(r,c+1,r+dr,c+1+dc)
            
            # If current is right side of box, move left side aswell
            if field[r][c] == BOX_RIGHT:
                move_item(r,c-1,r+dr,c-1+dc)
            
        return True

    if direction == EAST or direction == WEST:

        did_move = move(r+dr, c+dc, direction, act=act)
        if did_move:
            if act:
                move_item(r,c,r+dr,c+dc)
            return True
        return False
    
    raise Exception("Unhandled state")

print("Initial position", cur_row, cur_col)

# for direction in [WEST, SOUTH, WEST, NORTH, NORTH]:
for direction in moves:
    dir = directions[direction]
    did_move = move(cur_row, cur_col, direction, act=True)
    if did_move:
        cur_row += dir[0]
        cur_col += dir[1]
    if not is_test:
        print("Move:", direction)
        print("Pos", cur_row, cur_col)
        print_matrix(field)

print_matrix(field)
gps_sum = 0
for r in range(ROWS):
    for c in range(COLUMNS):
        if field[r][c] == BOX_LEFT:
            gps_sum += 100 * r + c
print("GPS sum:", gps_sum)
