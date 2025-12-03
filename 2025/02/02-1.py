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
ranges = data[0].split(',')

def chunks(l, n):
    for i in range(0, len(l), n):
        yield l[i:i+n]

def has_repeats(x: int):
    s = str(x)
    mid = len(s)//2
    first_half = s[0:mid]
    second_half = s[mid:]
    if first_half == second_half:
        return True
    return False


score = 0

for r in ranges: 
    first, last = [int(x) for x in r.split('-')]
    myrange = range(first, last+1,1)
    for x in myrange:
        if has_repeats(x):
            score += x


print(score)