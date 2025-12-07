# Load data

import sys
import re
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
data = [re.split(r'\s+', x) for x in data]
# print(data)

rows = len(data)
cols = len(data[0])

score = 0

for c in range(cols):
    # print(c, data[-1])
    sign = data[-1][c]

    numbers = [int(data[r][c]) for r in range(rows-1)]

    if sign == '+':
        score += sum(numbers)
    else:
        score += math.prod(numbers)

print("Score", score)


