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

SIZE = len(data)

def print_matrix(matrix):
    for row in range(len(matrix)):
        for col in range(len(matrix)):
            print(matrix[row][col], end=" ")
        print()

def print_imatrix(matrix):
    # Prerun
    maxnum = 0
    for row in range(len(matrix)):
        for col in range(len(matrix)):
            maxnum = max(maxnum, matrix[row][col])

    maxlen = len(str(maxnum))
    for row in range(len(matrix)):
        for col in range(len(matrix)):
            print(str(matrix[row][col]).zfill(maxlen), end=" ")
        print()


# Problem solution
from collections import namedtuple
import queue
import json

field = [[c for c in s.strip()] for s in data]
if not is_test:
    print_matrix(field)

def mget(r,c, matrix):
    if r >= 0 and r < SIZE and c >= 0 and c < SIZE:
        return matrix[r][c]
    return None

# Compute regions
region_counter = -1
region = [[-1 for _ in range(SIZE)] for _ in range(SIZE)]
region_plants = {}
region_info = {}
directions = [(-1,0), (0, 1), (1, 0), (0, -1)]


def get_neighbors(r,c):
    return [(r+dr,c+dc) for (dr,dc) in directions if r+dr >= 0 and r+dr < SIZE and c+dc >= 0 and c+dc < SIZE]

for r in range(SIZE):
    for c in range(SIZE):

        if region[r][c] != -1:
            continue      

        # Spread ID with BFS of same plant
        Q = queue.Queue()
        Q.put((r,c))
        visited = set()
        region_id = None

        while not Q.empty():
            cr, cc = Q.get() # Current row and coumns

            if (cr,cc) in visited:
                continue
            visited.add((cr,cc))

            # If current element already has region defined
            if region[cr][cc] != -1:
                region_id = region[cr][cc]

            # Check neighbors if they are same plant
            for (nr, nc) in get_neighbors(cr, cc):
                if field[nr][nc] == field[r][c]:
                    Q.put((nr,nc))

        # If no region ID was found, create
        if region_id is None:
            region_counter += 1
            region_id = region_counter
            region_info[region_id] = {}
        
        for (cr,cc) in visited:
            region[cr][cc] = region_id

        region_info[region_id]["plant"] = field[r][c]

        rows, cols = list(zip(*visited))
        region_info[region_id]["area"] = len(visited)
        region_info[region_id]["row_start"] = min(rows)
        region_info[region_id]["row_end"] = max(rows)
        region_info[region_id]["col_start"] = min(cols)
        region_info[region_id]["col_end"] = max(cols)

if not is_test:
    print("Region map:")
    print_imatrix(region)

# Compute sides
Sides = namedtuple("Sides", ["north", "east", "south", "west"])

# N, E, S, W
directions = [(-1,0), (0, 1), (1, 0), (0, -1)]

def print_Sides_matrix(matrix: list[list[Sides]]):
    for row in range(len(matrix)):
        for col in range(len(matrix)):
            sides = matrix[row][col]
            print(f"({int(sides.north)}{int(sides.east)}{int(sides.south)}{int(sides.west)})", end=" ")
        print()

perimeter:list[list[Sides]] = [[None for _ in range(SIZE)] for _ in range(SIZE)]

for r in range(SIZE):
    for c in range(SIZE):

        neighbor_regions = [mget(r+dr, c+dc, region) for (dr, dc) in directions]
        perimeter[r][c] = Sides(
            neighbor_regions[0] != region[r][c],
            neighbor_regions[1] != region[r][c],
            neighbor_regions[2] != region[r][c],
            neighbor_regions[3] != region[r][c]
        )

if not is_test:
    print("Perimeter map:")
    print_Sides_matrix(perimeter)

def bool_true_groups(lst: list[bool]):
    active = False
    groups = 0
    for b in lst:
        if not active and b:
            groups += 1
        active = b
    return groups

for region_id, info in region_info.items():

    region_num_sides = 0
    # Check horizontals
    for r in range(info["row_start"], info["row_end"]+1):
        col_interval = range(info["col_start"],info["col_end"]+1)
        sides = [perimeter[r][c] if region[r][c] == region_id else Sides(0,0,0,0) for c in col_interval ]
        region_num_sides += bool_true_groups([s.north for s in sides])
        region_num_sides += bool_true_groups([s.south for s in sides])
    # Chek verticals
    for c in range(info["col_start"], info["col_end"]+1):
        row_interval = range(info["row_start"], info["row_end"]+1)
        sides = [perimeter[r][c] if region[r][c] == region_id else Sides(0,0,0,0) for r in row_interval ]
        region_num_sides += bool_true_groups([s.east for s in sides])
        region_num_sides += bool_true_groups([s.west for s in sides])
    
    region_info[region_id]["sides"] = region_num_sides

if not is_test:
    print("Region info:")
    print(json.dumps(region_info, indent=2))

# Compute costs
s = 0
for id, info in region_info.items():
    s += info["area"] * info["sides"]

print("Total cost", s)

