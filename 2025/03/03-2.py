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

def debug(*args):
    if not is_test:
        print(args)

# Problem solution
def concat(x: int, y: int):
    return int(str(x) + str(y))

def max_joltage(numbers: list[int], n_digits):
    if n_digits == 1:
        return max(numbers)
    
    maxdigit = max(numbers[:-(n_digits-1)])
    maxidx = numbers.index(maxdigit)
    debug(numbers, maxdigit, maxidx)

    left = maxdigit
    right = max_joltage(numbers[maxidx+1:], n_digits - 1)
    return concat(left, right)

score = 0
for bank in data:
    numbers = [int(x) for x in bank]
    num = max_joltage(numbers, 12)
    print(bank, num)
    score += num

print("Score", score)
    