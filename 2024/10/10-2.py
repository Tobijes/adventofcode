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

# Problem solution
import queue
# Convert data
topmap = [[int(c) for c in s.strip()] for s in data]
print_matrix(topmap)

# Find trailheads
trailheads = []
for i, row in enumerate(topmap):
    for j, value in enumerate(row):
        if value == 0:
            trailheads.append((i,j))    
print("Trailheads", trailheads)

# BFS
def bfs_score(trailhead):

    Q = queue.Queue()

    paths: list[list[tuple[int,int]]] = []

    Q.put([trailhead])

    while not Q.empty():
        # print("Queue", list(Q.queue))
        path = Q.get()
        r, c = path[-1]
        # if visited[r][c] == 1:
        #     continue

        # visited[r][c] = 1
        value = topmap[r][c]

        # Check for peak
        if value == 9:
            paths.append(path)
            continue

        # West is up
        if r > 0 and topmap[r-1][c] == value + 1:
            Q.put(path + [(r-1, c)])

        # East is up
        if r < SIZE-1 and topmap[r+1][c] == value + 1:
            Q.put(path + [(r+1, c)])

        # North is up
        if c > 0 and topmap[r][c-1] == value + 1:
            Q.put(path + [(r, c-1)])

        # South is up
        if c < SIZE-1 and topmap[r][c+1] == value + 1:
            Q.put(path + [(r, c+1)])

    return paths

paths = sum([bfs_score(trailhead) for trailhead in trailheads], [])
# for path in paths:
#     print(path)
print("Final score", len(paths))