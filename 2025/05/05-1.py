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
split = data.index('')
ranges = data[:split]
ids = data[split+1:]
ranges = [r.split('-') for r in ranges]
ranges = [(int(r[0]), int(r[1])) for r in ranges]
ids = [int(x) for x in ids]
print(ranges)
print(ids)

score = 0
for id in ids:
    for (lower, upper) in ranges:
        if lower <= id and id <= upper:
            score += 1
            break

print("Score", score)