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
            print(matrix[row][col], end=" ")
        print()

# Problem solution
import queue
from enum import Enum
field = [list(s) for s in data]
print_matrix(field)

SIZE = len(field)
WALL = "#"
START = "S"
END = "E"
EMPTY = "."

class Direction(str, Enum):
    NORTH = "^"
    EAST = ">"
    SOUTH = "v"
    WEST = "<"

directions = {
    Direction.NORTH : (-1, 0),
    Direction.EAST : (0, 1),
    Direction.SOUTH : (1, 0),
    Direction.WEST : (0, -1)
}
clockwise = {
    Direction.NORTH : Direction.EAST,
    Direction.EAST : Direction.SOUTH,
    Direction.SOUTH : Direction.WEST, 
    Direction.WEST : Direction.NORTH
}
counter_clockwise = {
    Direction.NORTH : Direction.WEST,
    Direction.EAST : Direction.NORTH,
    Direction.SOUTH : Direction.EAST, 
    Direction.WEST : Direction.SOUTH
}

# Find start
def find_first(symbol):
    for r in range(SIZE):
        for c in range(SIZE):
            if field[r][c] == symbol:
                return r, c
            
    raise Exception("Could not find start")

PosDir = tuple[int, int, Direction]
Path = list[PosDir]
Visited = set[PosDir]

def min_nonable(lst: list[int]):
    lst = [a for a in lst if a is not None]

    if len(lst) == 0:
        return None
    
    return min(lst)

def print_path(path: Path):
    path_map = [["" for _ in range(SIZE)] for _ in range(SIZE)]
    for row in range(len(field)):
        for col in range(len(field[0])):
            path_map[row][col] = field[row][col]
    

    for r,c,d in path:
        path_map[r][c] = d.value
    print_matrix(path_map)


scores = [[None for _ in range(SIZE)] for _ in range(SIZE)]

Q = queue.Queue()

r_start, c_start = find_first(START)
r_end, c_end = find_first(END)
Q.put((r_start,c_start,Direction.EAST, 0))

while not Q.empty():

    r,c,dir,cost = Q.get()

    if field[r][c] == WALL:
        continue

    if scores[r][c] is not None and scores[r][c] < cost:
        continue

    scores[r][c] = cost

    if field[r][c] == END:
        continue

    # Forward
    d = dir
    dr,dc = directions[d]
    Q.put((r+dr, c+dc, d, cost + 1))

    # Clockwise
    d = clockwise[dir]
    dr,dc = directions[d]
    Q.put((r+dr, c+dc, d, cost + 1001))

    # Counter clockwise
    d = counter_clockwise[dir]
    dr,dc = directions[d]
    Q.put((r+dr, c+dc, d, cost + 1001))

print_matrix(scores)

print("Min score", scores[r_end][r_start])

