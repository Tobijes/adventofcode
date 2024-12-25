# Load data

import sys

if len(sys.argv) > 1 and sys.argv[1] == "t":
    with open("input.txt") as f:
        data =  f.readlines()
else:
    with open("sample.txt") as f:
        data =  f.readlines()

SIZE = len(data)

def print_matrix(matrix):
    for row in range(len(matrix)):
        for col in range(len(matrix)):
            print(matrix[row][col], end="")
        print()

# Problem solution