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
            print(matrix[row][col], end="")
        print()

# Problem solution