# Load data

import sys

if len(sys.argv) > 1 and sys.argv[1] == "t":
    with open("input.txt") as f:
        data =  list(f.readlines())
else:
    with open("sample.txt") as f:
        data =  list(f.readlines())

SIZE = len(data)

def print_matrix(matrix):
    for row in range(len(matrix)):
        for col in range(len(matrix)):
            print(matrix[row][col], end="")
        print()

# Problem solution
import itertools
antennas = {}

for row in range(SIZE):
    for col in range(SIZE):
        letter = data[row][col]
        if letter != '.':
            if letter in antennas:
                antennas[letter].append((row,col))
            else:
                antennas[letter] = [(row,col)]
print(antennas)

antinodes = []
valid = lambda x: x[0] >= 0 and x[0] < SIZE and x[1] >= 0 and x[1] < SIZE

for frequency in antennas:
    pairs = list(itertools.combinations(antennas[frequency], 2))
    for (x1,y1),(x2,y2) in pairs:

        xDiff = x1 - x2
        yDiff = y1 - y2
        
        for i in range(10000):
            an = (x1+(i*xDiff), y1+(i*yDiff))
            if valid(an):
                antinodes.append(an)
            else:
                break

        for i in range(10000):    
            an = (x2-(i*xDiff), y2-(i*yDiff))
            if valid(an):
                antinodes.append(an)
            else:
                break

print(antinodes)

map = [['.' for col in range(SIZE)] for row in range(SIZE)]
for (r,c) in antinodes:
    map[r][c] = '#'

print_matrix(data)
print()
print_matrix(map)

print(len(set(antinodes)))