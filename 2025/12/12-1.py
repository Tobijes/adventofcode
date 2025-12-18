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
for i in range(0, 30, 5):
    rows = data[i+1:i+4]
    figure = [1 if c == '#' else 0 for c in "".join(rows)]
    figure = tuple(figure)
    figure = tuple2bitrect(figure, 3)
    figures.append(figure)

regions = []
for i in range(30, len(data)):
    print(data[i])
    left, right = data[i].split(": ")
    width, height = [int(x) for x in left.split("x")]
    quantities = [int(x) for x in right.split(" ")]
    regions.append(Region(width, height, quantities))


figure_permutations = [permutations(figure) for figure in figures]

# Print all figure permutations
for i, variations in enumerate(figure_permutations):
    width = len(variations) * (3+1) + 1
    height = 5
    print(f"{i=}")

    plane = BitRect(0, width*height, width)

    for j, variation in enumerate(variations):
        
        projection = project_bitrect(variation, 1+(j*(figure.width+1)), 1, width, height)
        plane = add(plane, projection)
    
    print_bitrect(plane)





region = regions[2]
blocks = quantities2elements(region.quantities)
print(blocks)

def place_blocks(current, missing_blocks):
    if len(missing_blocks) == 0:
        print("Solution!", current)
        return current
    

    for x in range(region.width-2):
        for y in range(region.height-2):
            projection = project_bitrect(missing_blocks[0], x, y, region.width, region.height)
            if has_collision(current, projection):
                continue
            
            next = add(current, projection)

            solution = place_blocks(next, missing_blocks[1:] )
            if solution:
                return solution
    return None

print("# of blocks: ",len(blocks))
block_variations = [figure_permutations[block] for block in blocks]
combinations = [list(x) for x in itertools.product(*[figure_permutations[block] for block in blocks])]
print("# of combiations: ", len(combinations))
for i,combination in enumerate(combinations):
    print(f"{i=}/{len(combinations)}")
    print(combination)
    current = BitRect(0, region.width*region.height, region.width)
    solution = place_blocks(current, combination)
    # print(solution)
    

# ON THE WAY TO EXTREMELY OVERKILL SOLUTION FOR INPUT...
