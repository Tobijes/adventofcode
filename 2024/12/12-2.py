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
for r in range(SIZE):
    for c in range(SIZE):
        print(r,c)

        # If no region id, observe if neighbors of same plant has region ID
        if region[r][c] == -1:
            connected_fields = [mget(r+dr, c+dc, field) for (dr, dc) in directions]
            connected_regions = [mget(r+dr, c+dc, region) for (dr, dc) in directions]
            for i in range(len(directions)):
                if connected_fields[i] == field[r][c]: #same plant
                    if connected_regions[i] != -1: #other plant already has region id
                        region[r][c] = connected_regions[i]
                        break
        
        # If not neighbors had id, create ID
        if region[r][c] == -1:
            region_counter += 1
            region[r][c] = region_counter
            region_plants[region_counter] = field[r][c]
        

        # Spread ID with BFS of same plant
        Q = queue.Queue()
        Q.put((r,c))
        visited = set()

        while not Q.empty():
            nr, nc = Q.get()

            if (nr,nc) in visited:
                continue
            visited.add((nr,nc))

            region[nr][nc] = region[r][c]
            connected_fields = [mget(nr+dr, nc+dc, field) for (dr, dc) in directions]
            for i in range(len(directions)):
                if connected_fields[i] is not None and connected_fields[i] == field[r][c]: #same plant
                    dr, dc = directions[i]
                    new_pos = (nr+dr, nc+dc)
                    if region[new_pos[0]][new_pos[1]] == -1:
                        Q.put((nr+dr,nc+dc))


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