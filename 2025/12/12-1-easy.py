from dataclasses import dataclass
import itertools
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
@dataclass(slots=True)
class BitRect:
    bits: int
    length: int
    width: int

@dataclass
class Region:
    width: int
    height: int
    quantities: list[int]

def print_bitrect(br: BitRect, exist='#', noexist='.'):
    t = bitrect2tuple(br)
    width = br.width
    height = br.length // width

    for i in range(height):
        for j in range(width):
            if t[i*width+j] == 1:
                print(exist, end="")
            else:
                print(noexist, end="")
        print()

def tuple2bitrect(t: tuple[int], width):
    bits = int(''.join(map(str, t)), 2)
    return BitRect(bits=bits, length=len(t), width=width)

def bitrect2tuple(br: BitRect):
    bit_string = bin(br.bits)[2:].zfill(br.length)
    bit_tuple = tuple(int(b) for b in bit_string)
    return bit_tuple

def quantities2elements(quantities):
    elements = []
    for i in range(len(quantities)):
        count = quantities[i]
        elements += [i] * count
    return elements

def permutations(figure: BitRect):

    t = bitrect2tuple(figure)

    # 0 1 2    2 1 0
    # 3 4 5 -> 5 4 3
    # 6 7 8    8 7 6
    flip = lambda f: (f[2], f[1], f[0], f[5], f[4], f[3], f[8], f[7], f[6])

    # 0 1 2    2 5 8
    # 3 4 5 -> 1 4 7
    # 6 7 8    0 3 6
    rotate90 = lambda f: (f[2], f[5], f[8], f[1], f[4], f[7], f[0], f[3], f[6])

    original = t   
    original90 = rotate90(original)
    original180 = rotate90(original90)
    original270 = rotate90(original180)

    flipped = flip(original)
    flipped90 = rotate90(flipped)
    flipped180 = rotate90(flipped90)
    flipped270 = rotate90(flipped180)

    uniques = set([original, original90, original180, original270, flipped, flipped90, flipped180, flipped270])

    return [tuple2bitrect(x, 3) for x in uniques]


def project_bitrect(figure: BitRect, x, y, width, height):
    if x + 3 > width:
        raise Exception("shape out of bounds x")
    if y + 3 > height:
        raise Exception("shape out of bounds y")
    
    f_width = 3

    start_pad = y*width + x
    mid_pad = width - f_width
    end_pad = (width * height) - (start_pad + f_width * 3 + mid_pad * 2)

    top = (figure.bits >> 6) & 0b111
    mid = (figure.bits >> 3) & 0b111
    bot = (figure.bits) & 0b111

    bits = top
    bits = bits << (mid_pad + f_width)
    bits = bits | mid
    bits = bits << (mid_pad + f_width)
    bits = bits | bot
    bits = bits << end_pad

    return BitRect(bits=bits, width=width, length=width*height)

def has_collision(a: BitRect, b: BitRect):
    return a.bits & b.bits > 0

def add(a: BitRect, b: BitRect):
    if a.length != b.length:
        raise Exception("a and b does not have same length")
    
    if a.width != b.width:
        raise Exception("a and b does not have same width")
    
    bits = a.bits | b.bits
    return BitRect(bits=bits, length=a.length, width=a.width)

figures = []
areas = []
for i in range(0, 30, 5):
    rows = data[i+1:i+4]
    figure = [1 if c == '#' else 0 for c in "".join(rows)]
    areas.append(sum(figure))

    figure = tuple(figure)
    figure = tuple2bitrect(figure, 3)
    figures.append(figure)
print(areas)
regions = []
for i in range(30, len(data)):
    print(data[i])
    left, right = data[i].split(": ")
    width, height = [int(x) for x in left.split("x")]
    quantities = [int(x) for x in right.split(" ")]
    regions.append(Region(width, height, quantities))

score = 0
for region in regions:
    total_area = 0
    for i,quantity in enumerate(region.quantities):
        total_area += quantity * areas[i]
    if total_area < region.width * region.height:
        print(True)
        score += 1

print(f"{score=}")
