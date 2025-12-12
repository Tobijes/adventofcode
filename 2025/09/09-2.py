# Load data

import sys
from dataclasses import dataclass

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
@dataclass(frozen=True)
class Point():
    x: int
    y: int

@dataclass(frozen=True)
class LineSegment():
    a: Point
    b: Point

data = [Point(*list(map(int,l.split(",")))) for l in data]

line_segments = []
for i in range(len(data)):
    if i < len(data) - 1:
        line_segments.append(LineSegment(data[i], data[i+1]))
    else:
        line_segments.append(LineSegment(data[i], data[0]))

if not is_test:
    print(data)
    print(line_segments)

def area(p1: Point, p2: Point):
    width = abs(p1.x-p2.x) + 1 
    height = abs(p1.y-p2.y) + 1
    return width * height

# Wiki: https://en.wikipedia.org/wiki/Line%E2%80%93line_intersection
def cross(l1: LineSegment, l2: LineSegment):
    x1, x2, x3, x4 = l1.a.x, l1.b.x, l2.a.x, l2.b.x
    y1, y2, y3, y4 = l1.a.y, l1.b.y, l2.a.y, l2.b.y
    if len(set([l1.a, l1.b, l2.a, l2.b])) < 4:
        return False
    try:
        t = ( (x1-x3) * (y3-y4) - (y1-y3) * (x3-x4) ) / ( (x1-x2) * (y3-y4) - (y1-y2) * (x3-x4) )
        u = -( (x1-x2) * (y1-y3) - (y1-y2) * (x1-x3) ) / ( (x1-x2) * (y3-y4) - (y1-y2) * (x3-x4) )
    except ZeroDivisionError:
        return False
    # print( t,u)
    return 0 <= t and t <= 1 and 0 <= u and u <= 1

def points_between(p1: Point, p2: Point):
    if p1.x == p2.x:
        miny = min(p1.y, p2.y)
        maxy = max(p1.y, p2.y)

        return [Point(p1.x, y) for y in range(miny, maxy+1)]
    elif p1.y == p2.y:
        minx = min(p1.x, p2.x)
        maxx = max(p1.x, p2.x)

        return [Point(x, p1.y) for x in range(minx, maxx+1)]
    else:
        raise Exception("Not horz/vert")

def rect_between(p1: Point, p2: Point):
    return [
        LineSegment(p1, Point(p2.x, p1.y)),
        LineSegment(p1, Point(p1.x, p2.y)),
        LineSegment(p2, Point(p1.x, p2.y)),
        LineSegment(p2, Point(p2.x, p1.y)),
    ]

def draw(objs: list, size):
    image = [['.' for _ in range(size)] for _ in range(size)]
    for o in objs:
        if isinstance(o, Point):
            image[o.y][o.x] = '#'
        elif isinstance(o, LineSegment):
            for p in points_between(o.a, o.b):
                image[p.y][p.x] = 'X'
            image[o.a.y][o.a.x] = '#'
            image[o.b.y][o.b.x] = '#'
    print_matrix(image)

# draw(line_segments, 15)
test_lines = [
    LineSegment(Point(1,1), Point(1,5)),
    LineSegment(Point(1,1), Point(5,1))
]

test_lines = rect_between(Point(1,2), Point(7,8))
test_lines += [LineSegment(Point(4,8), Point(5,8)),]

draw(test_lines, 10)

for line in test_lines[:-1]:

    print(line, cross(line, test_lines[-1]))

# if not is_test:
#     draw(line_segments, 15)
# maxarea = 0
# maxpoints = (0,0)
# for i in range(len(data)):
#     print(f"{i=}/{len(data)} {maxarea=}")
#     for j in range(i+1, len(data)):
#         p1 = data[i]
#         p2 = data[j]
        
#         has_cross = False
#         for rect_line in rect_between(p1, p2):
#             if has_cross:
#                 break

#             for line in line_segments:
#                 if cross(rect_line, line):
#                     has_cross = True
#                     break


#         if has_cross:
#             continue

#         a = area(p1, p2) 
#         if a > maxarea:
#             maxarea = a
#             maxpoints = (i,j)

# print(maxarea, data[maxpoints[0]],data[maxpoints[1]])