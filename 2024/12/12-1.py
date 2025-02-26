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
import queue
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
            region_plants[region_counter] = field[r][c]
        
        for (cr,cc) in visited:
            region[cr][cc] = region_id

if not is_test:
    print("Region map:")
    print_imatrix(region)

# Compute perimeters
perimeter = [[0 for _ in range(SIZE)] for _ in range(SIZE)]

# N, E, S, W
directions = [(-1,0), (0, 1), (1, 0), (0, -1)]
for r in range(SIZE):
    for c in range(SIZE):
        cur_region = region[r][c]

        connections = [mget(r+dr, c+dc, region) for (dr, dc) in directions]

        others = [region for region in connections if region != cur_region]
        perimeter[r][c] = len(others)

if not is_test:
    print("Perimeter map:")
    print_imatrix(perimeter)

# Compute costs
region_area = {}
region_perimeters = {}

for r in range(SIZE):
    for c in range(SIZE):
        region_id = region[r][c]
        
        plot_area = 1
        if region_id in region_area:
            region_area[region_id] += plot_area
        else:
            region_area[region_id] = plot_area

        plot_perimeter = perimeter[r][c]
        if region_id in region_perimeters:
            region_perimeters[region_id] += plot_perimeter
        else:
            region_perimeters[region_id] = plot_perimeter

if not is_test:
    print("Region plants", region_plants)
    print("Total Areas", region_area)
    print("Total Perimeter", region_perimeters)


assert region_area.keys() == region_perimeters.keys()

s = 0
for region in region_area:
    s += region_area[region] * region_perimeters[region]

print("Total cost", s)

# for id, plant in region_plants.items():
#     print(plant, region_area[id], region_perimeters[id], region_area[id] * region_perimeters[id])