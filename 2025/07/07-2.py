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
            print(matrix[row][col], end="")
        print()

# Problem solution
width = len(data[0])
height = len(data)

data = [list(d) for d in data]
print_matrix(data)

def beam(row, col):

    if row == height:
        return 1

    if isinstance(data[row][col], int):
        return data[row][col]

    if data[row][col] == '^':
        left = beam(row, col-1)
        right = beam(row, col+1)
        return left + right
    elif data[row][col] == '.':
        down = beam(row+1, col)
        data[row][col] = down
        return down
    else:
        return 0


start = data[0].index('S')
print(start)

score = beam(1, start)
print_matrix(data)
print("Score", score)