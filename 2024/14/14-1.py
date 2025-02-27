# Load data

import sys

is_test = len(sys.argv) > 1 and sys.argv[1] == "t"
print("IS TEST:", is_test)

if is_test:
    with open("input.txt") as f:
        data =  f.readlines()
else:
    with open("sample.txt") as f:
        data =  f.readlines()
        
data = [l.strip() for l in data]
SIZE = len(data)

def print_matrix(matrix):
    for row in range(len(matrix)):
        for col in range(len(matrix)):
            print(matrix[row][col], end=" ")
        print()

# Problem solution
from dataclasses import dataclass
import re

ROWS = 7
COLUMNS = 11

if is_test:
    ROWS = 103
    COLUMNS = 101

@dataclass
class Robot:
    r: int
    c: int
    vr: int
    vc: int

def print_robots(robots: list[Robot]):
    robots_at_position = [[0 for _ in range(COLUMNS)] for _ in range(ROWS)]

    for robot in robots:
        robots_at_position[robot.r][robot.c] += 1

    for row in range(ROWS):
        for col in range(COLUMNS):
            print(robots_at_position[row][col] if robots_at_position[row][col] > 0 else "." , end="")
        print()

robots: list[Robot] = []

for line in data:
    x,y,vx,vy = re.search(r"p=(\d+),(\d+) v=([0-9\-]+),([0-9\-]+)", line).groups()
    robots.append(Robot(r=int(y), c=int(x), vr=int(vy), vc=int(vx)))

print(robots)

def get_new_position(robot: Robot):

    new_r = robot.r + robot.vr
    new_c = robot.c + robot.vc
    # print("Before wrapping", new_r, new_c)

    if new_r < 0:
        new_r = ROWS + new_r

    if new_r >= ROWS:
        new_r = new_r - ROWS

    if new_c < 0:
        new_c = COLUMNS + new_c

    if new_c >= COLUMNS:
        new_c = new_c - COLUMNS
    # print("After wrapping", new_r, new_c)
    return new_r, new_c

print("Start")
print_robots(robots)

for i in range(100):
    for robot in robots:
        new_r, new_c = get_new_position(robot)
        robot.r = new_r
        robot.c = new_c
    print(f"{i=}")
    print_robots(robots)

# Compute Safety Factor
robots_at_position = [[0 for _ in range(COLUMNS)] for _ in range(ROWS)]

for robot in robots:
    robots_at_position[robot.r][robot.c] += 1

mid_row = ROWS // 2
mid_col = COLUMNS // 2

q1 = sum([robots_at_position[r][c] for r in range(0, mid_row) for c in range(mid_col+1, COLUMNS)])
q2 = sum([robots_at_position[r][c] for r in range(0, mid_row) for c in range(0, mid_col)])
q3 = sum([robots_at_position[r][c] for r in range(mid_row+1, ROWS) for c in range(0, mid_col)])
q4 = sum([robots_at_position[r][c] for r in range(mid_row+1, ROWS) for c in range(mid_col+1, COLUMNS)])
print("Quadrant numbers", q1,q2,q3,q4)
print("Safety Factor", q1*q2*q3*q4)