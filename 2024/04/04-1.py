# Load data

import sys

with open("input.txt") as f:
    file_input = f.read()

with open("sample.txt") as f:
    file_sample = f.read()

data = file_sample

if len(sys.argv) > 1 and sys.argv[1] == "t":
    data = file_input

# Problem solution

# Load data
lines = data.split()
print(lines)
SIZE = len(lines)
WORD="XMAS"

dirs = [
    (-1,-1),(1,1),(1,-1),(-1,1),
    (-1,0),(1,0),(0,1),(0,-1)
]

def boundary_check(row, col, dir):
    dr, dc = dir
    nr = row + dr
    nc = col + dc
    valid = lambda x: x >= 0 and x < SIZE
    return valid(nr) and valid(nc)


def search_dir(row, col, dir, subword):
    subword += lines[row][col]


    # Check if word found
    if subword == WORD:
        return 1
    
    # Check if invalid prefix
    if not WORD.startswith(subword):
        return 0
    
    # Check if next position is valid
    if not boundary_check(row, col, dir):
        return 0
    
    dr, dc = dir
    return search_dir(row+dr,col+dc,dir,subword)

total_count = 0
for row in range(SIZE):
    for col in range(SIZE):
        candidate_dirs = filter(lambda d: boundary_check(row, col, d), dirs)
        for dir in candidate_dirs:
            total_count += search_dir(row,col, dir,"")

print(total_count)
