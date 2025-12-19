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
@dataclass(frozen=True, slots=True)
class Point():
    x: int
    y: int

@dataclass(frozen=True, slots=True)
class LineSegment():
    a: Point
    b: Point

def area(p1: Point, p2: Point):
    width = abs(p1.x-p2.x) + 1 
    height = abs(p1.y-p2.y) + 1
    return width * height

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


canvas_points = []

def canvas_reset():
    canvas_points.clear()

def canvas_point(p: Point, c = '#'):
    canvas_points.append((p.x, p.y, c))

def canvas_line(l: LineSegment, lc = 'X', ec = '#'):
    for p in points_between(l.a, l.b):
        canvas_points.append((p.x, p.y, lc))
    canvas_points.append((l.a.x, l.a.y, ec))
    canvas_points.append((l.b.x, l.b.y, ec))

def canvas_draw():
    maxx = max([d[0] for d in canvas_points])
    maxy = max([d[1] for d in canvas_points])

    image = [['.' for _ in range(maxx+2)] for _ in range(maxy+2)]

    for x, y, c in canvas_points:
        image[y][x] = c
    print_matrix(image)

def canvas_draw_scaled(width):
    maxx = max([d[0] for d in canvas_points])
    maxy = max([d[1] for d in canvas_points])

    scale = width / maxx

    image = [['.' for _ in range(width+1)] for _ in range(round(maxy*scale)+2)]

    for x, y, c in canvas_points:
        x_scaled = round(x * scale)
        y_scaled = round(y * scale)
        image[y_scaled][x_scaled] = c
    print_matrix(image)

data = [[int(x) for x in d.split(",")]  for d in data]
data = [Point(d[0], d[1]) for d in data]

line_segments: list[LineSegment] = []
for i in range(len(data)):
    if i < len(data) - 1:
        line_segments.append(LineSegment(data[i], data[i+1]))
    else:
        line_segments.append(LineSegment(data[i], data[0]))

def clamp_point(p: Point, minx: int, maxx: int, miny: int, maxy: int):
    return Point(min(max(minx, p.x), maxx), min(max(miny, p.y), maxy))

def point_on_line(p: Point, l: LineSegment):
    return min(l.a.x, l.b.x) <= p.x <= max(l.a.x, l.b.x) and min(l.a.y, l.b.y) <= p.y <= max(l.a.y, l.b.y)

def is_rect_valid(p1: Point, p2: Point):
    minx = min(p1.x, p2.x)
    maxx = max(p1.x, p2.x)
    miny = min(p1.y, p2.y)
    maxy = max(p1.y, p2.y)

    for p in data:
        if minx < p.x < maxx and miny < p.y < maxy:
            return False

    # Clamp line segments and check if on it
    has_3 = False
    has_4 = False
    p3 = Point(p1.x, p2.y) 
    p4 = Point(p2.x, p1.y)

    # print(minx,maxx,miny,maxy)
    # print(p3, p4)


    # canvas_reset()

    for l in line_segments:
        a_clamped = clamp_point(l.a, minx, maxx, miny, maxy)
        b_clamped = clamp_point(l.b, minx, maxx, miny, maxy)

        line_clamped = LineSegment(a_clamped, b_clamped)

        if a_clamped.x != b_clamped.x and miny < a_clamped.y < maxy and miny < b_clamped.y < maxy:
            return False

        # canvas_line(line_clamped)
        has_3 |= point_on_line(p3, line_clamped)
        has_4 |= point_on_line(p4, line_clamped)
        # print("3", has_3, p3, line_clamped)
        # print("4", has_4, p4, line_clamped)
        if has_3 and has_4:
            return True


    # canvas_point(p1, 'O')
    # canvas_point(p2, 'O')
    # canvas_point(p3, 'Ø')
    # canvas_point(p4, 'Ø')

    # canvas_draw()
    # print(f"{has_3} {has_4}")

    return has_3 and has_4

canvas_reset()
for line in line_segments:
    canvas_line(line)


# print(data)
maxarea = 0
maxpoints = (None,None)
for i in range(len(data)):
    print(f"{i=}/{len(data)} {maxarea=}")
    for j in range(i+1, len(data)):
        p1 = data[i]
        p2 = data[j]

        a = area(p1, p2) 
        if a < maxarea:
            continue

        if not is_rect_valid(p1, p2):
            continue

        maxarea = a
        maxpoints = (p1,p2)

print(maxarea, maxpoints[0], maxpoints[1])

# print(is_rect_valid(Point(2,3), Point(9,5)))
# print(point_on_line(Point(2,5), LineSegment(Point(2,5), Point(5,5))))
canvas_point(maxpoints[0], "O")
canvas_point(maxpoints[1], "O")
canvas_draw_scaled(150)
