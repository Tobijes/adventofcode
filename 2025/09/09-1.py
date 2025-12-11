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
data = [tuple(map(int,l.split(","))) for l in data]

def area(p1, p2):
    width = abs(p1[0]-p2[0]) + 1 
    height = abs(p1[1]-p2[1]) + 1
    return width * height

print(data)

maxarea = 0
maxpoints = (0,0)
for i in range(len(data)):
    for j in range(i+1, len(data)):
        a = area(data[i], data[j]) 
        if a > maxarea:
            maxarea = a
            maxpoints = (i,j)

print(maxarea, data[maxpoints[0]],data[maxpoints[1]])