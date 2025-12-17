from dataclasses import dataclass
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
@dataclass
class Region:
    width: int
    height: int
    quantities: list[int]

def print_figure(figure, exist='#', noexist='.'):
    for i in range(3):
        for j in range(3):
            if figure[i*3+j] == 1:
                print(exist, end="")
            else:
                print(noexist, end="")
        print()



# 0 1 2    2 1 0
# 3 4 5 -> 5 4 3
# 6 7 8    8 7 6
def flip(f):
    return (f[2], f[1], f[0], f[5], f[4], f[3], f[8], f[7], f[6])

# 0 1 2    2 5 8
# 3 4 5 -> 1 4 7
# 6 7 8    0 3 6
def rotate90(f):
    return (f[2], f[5], f[8], f[1], f[4], f[7], f[0], f[3], f[6])

def permutations(figure):
    original = figure   
    original90 = rotate90(original)
    original180 = rotate90(original90)
    original270 = rotate90(original180)

    flipped = flip(original)
    flipped90 = rotate90(flipped)
    flipped180 = rotate90(flipped90)
    flipped270 = rotate90(flipped180)

    return set([original, original90, original180, original270, flipped, flipped90, flipped180, flipped270])

def project(figure, x, y, width, height):
    if x + 3 > width:
        raise Exception("shape out of bounds x")
    if y + 3 > height:
        raise Exception("shape out of bounds y")
    start_pad = y*width + x
    mid_pad = width - 3
    end_pad = (width*height) - (start_pad + 3*mid_pad)

    figure = list(figure)

    return [0] * start_pad + figure[0:3] + [0] * mid_pad + figure[3:6] + [0] * mid_pad + figure[6:9] + [0] * end_pad

figures = []
for i in range(0, 30, 5):
    rows = data[i+1:i+4]
    figure = [1 if c == '#' else 0 for c in "".join(rows)]
    figure = tuple(figure)
    figures.append(figure)

regions = []
for i in range(30, len(data)):
    print(data[i])
    left, right = data[i].split(": ")
    width, height = [int(x) for x in left.split("x")]
    quantities = [int(x) for x in right.split(" ")]
    regions.append(Region(width, height, quantities))

# print(figures)
print_figure(figures[0])
# print(regions)
width = 12
height = 5
projection = project(figures[0], 9, 2, width, height)

for i in range(5):
    print(projection[i*width:(i+1)*width])
# region = regions[0]

# for i, f in enumerate(figures):
#     print(i)
#     variations = permutations(f)
#     for v in variations:
#         print_figure(v)
#         print()

# Definitely not done!
