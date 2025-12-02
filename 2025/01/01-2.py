# Load data

import sys
import math 

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
dial = 50
score = 0

def sign(x):
    if x > 0:
        return 1
    elif x < 0:
        return -1
    return 0

for cmd in data:
    dir = cmd[0]
    val = int(cmd[1:])

    # Handle higher than 100 numbers
    rounds = val // 100
    if rounds > 0:
        print("Adding", rounds, "rounds")
    score += rounds
    offset = val % 100
    signdir = 1 if dir == 'R' else -1
    moved_dial = dial + (signdir * offset)
    print("Before:", dial, "Input:", signdir, val, rounds, "Moved", moved_dial)
    if moved_dial % 100 == 0:
        print("Zero sharp!")
        score += 1
    elif sign(dial) != sign(moved_dial) and sign(dial) + sign(moved_dial) == 0:
        print("Zero cross", dial, moved_dial)
        score += 1
    elif moved_dial > 100:
        score += 1
    dial = moved_dial % 100
    print("After:", dial) 

print(score)
