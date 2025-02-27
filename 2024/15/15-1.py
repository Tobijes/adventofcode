# Load data

import sys

is_test = len(sys.argv) > 1 and sys.argv[1] == "t"
print("IS TEST:", is_test)

if is_test:
    with open("input.txt") as f:
        data =  f.readlines()
else:
    with open("sample.txt") as f:
        data =  f.readlines()
        
data = [l.strip() for l in data]

def print_matrix(matrix):
    for row in range(len(matrix)):
        for col in range(len(matrix)):
            print(matrix[row][col], end="")
        print()

# Problem solution
# Handle input data
dataset_splitter = data.index('')
field_lines = data[:dataset_splitter]
move_lines = data[dataset_splitter+1:]

SIZE = len(field_lines)

field = [list(s) for s in field_lines]
if not is_test:
    print("Field:")
    print_matrix(field)

moves = list("".join(move_lines))
if not is_test:
    print("Moves:")
    print(moves)

# Set up constants
EMPTY = "."
WALL = "#"
BOX = "O"
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

# Find initial position
def find_robot(field):
    for r in range(SIZE):
        for c in range(SIZE):
            if field[r][c] == ROBOT:
                return r, c
            

def move(r, c, direction):
    dr, dc = direction

    if field[r+dr][c+dc] == WALL:
        return False

    if field[r+dr][c+dc] == EMPTY:
        field[r+dr][c+dc] = field[r][c]
        field[r][c] = EMPTY
        return True

    if field[r+dr][c+dc] == BOX:
        did_move = move(r+dr, c+dc, direction)
        if did_move:
            field[r+dr][c+dc] = field[r][c]
            field[r][c] = EMPTY
            return True
        return False
    raise Exception("Unhandled state")

cur_row, cur_col = find_robot(field)
print("Initial position", cur_row, cur_col)

for movecmd in moves:
    dir = directions[movecmd]
    did_move = move(cur_row, cur_col, dir)
    if did_move:
        cur_row += dir[0]
        cur_col += dir[1]
    if not is_test:
        print("Move:", movecmd)
        print("Pos", cur_row, cur_col)
        print_matrix(field)

gps_sum = 0
for r in range(SIZE):
    for c in range(SIZE):
        if field[r][c] == BOX:
            gps_sum += 100 * r + c

print("GPS sum:", gps_sum)
