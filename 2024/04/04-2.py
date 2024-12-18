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
    (-1, -1),
    (-1, 1),
    (1, 1),
    (1, -1)
]

options = [
    "MSSM",
    "MMSS",
    "SMMS",
    "SSMM"
]

def check_patterns(row,col):
    for option in options:
        valid = True
        for i, (dr,dc) in enumerate(dirs):
            if lines[row+dr][col+dc] != option[i]:
                valid = False
                break
        if valid:
            return True
    return False


total_count = 0
for row in range(SIZE):
    for col in range(SIZE):
        letter = lines[row][col]
        # Ease search
        if letter == 'A' and row > 0 and row < SIZE - 1 and col > 0 and col < SIZE - 1:
            # Check
            if check_patterns(row, col):
                total_count += 1      

print(total_count)



"""
M S
 A
M S

M M
 A 
S S

S M
 A
S M

S S
 A
M M
"""