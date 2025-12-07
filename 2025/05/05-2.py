# Load data

import sys
from collections import namedtuple

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
Range = namedtuple('Range', ["start", "stop"])
split = data.index('')
ranges = data[:split]
ranges = [r.split('-') for r in ranges]
ranges = [Range(int(r[0]), int(r[1])) for r in ranges]
ranges = sorted(ranges, key=lambda x: x[0])
print(ranges)
unified_ranges = []
current = ranges[0]
for next in ranges[1:]:
    print(current, next)
    if next.start <= current.stop:
        current = Range(current.start, max(current.stop, next.stop))
        continue
    
    unified_ranges.append(current)
    current = next
unified_ranges.append(current) 
print(unified_ranges)

score = 0
for r in unified_ranges:
    score += (r.stop - r.start) + 1

print("Score", score)