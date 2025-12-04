# Load data

import sys
import copy

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
def add(p1, p2):
    r1,c1 = p1
    r2,c2 = p2
    return (r1+r2, c1+c2)

n = (0, -1)
e = (1, 0)
s = (0, 1)
w = (-1, 0)
nw = add(n,w)
ne = add(n,e)
se = add(s,e)
sw = add(s,w)

DIRS = [nw,n,ne,e,se,s,sw,w]

def isroll(r,c, data):
    rows = len(data)
    cols = len(data[0])

    if r < 0 or r >= rows:
        return False
    if c < 0 or c >= cols:
        return False
    
    if data[r][c] == '@':
        return True
    
    return False
    
data = [list(l) for l in data]
print_matrix(data)
score = 0

while True:
    removed = 0
    for r, row in enumerate(data):
        for c, col in enumerate(row):
            if not isroll(r,c, data):
                continue
            
            rolls = 0
            for dir in DIRS:
                dr, dc = add((r,c),dir)
                rolls += isroll(dr,dc, data)

            if rolls < 4:
                removed += 1
                data[r][c] = 'x'
    score += removed
    if removed == 0:
        break

print("Score", score)
