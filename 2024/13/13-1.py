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
data = [s for s in data if len(s) > 0]
print(data)

BUTTON_TOKENS_A = 3
BUTTON_TOKENS_B = 1

@dataclass
class Vec2():
    x: int
    y: int

@dataclass
class ClawMachine():
    a: Vec2
    b: Vec2
    goal: Vec2

claw_machines: list[ClawMachine] = []

# Parse input, assume format is strictly formed
for i in range(0, len(data), 3):
    button_a_line = data[i]
    button_b_line = data[i+1]
    goal_line = data[i+2]

    ax, ay = re.search(r".+: X.(\d+), Y.(\d+)", data[i]).groups()
    bx, by = re.search(r".+: X.(\d+), Y.(\d+)", data[i+1]).groups()
    gx, gy = re.search(r".+: X.(\d+), Y.(\d+)", data[i+2]).groups()
    
    claw_machines.append(ClawMachine(
        a    = Vec2(int(ax),int(ay)),
        b    = Vec2(int(bx),int(by)),
        goal = Vec2(int(gx),int(gy))
    ))

print(claw_machines)
""" Formulae
Eq 1: ax * x1 + bx * x2 = gx
Eq 2: ay * x1 + by * x2 = gy
A = [
ax bx
ay by
]
b = [
gx
gy
]
A . x = b

finding x -> innversion of 2x2 matrices 
x = A^-1 . b
"""

def mat2_det(m11, m12, m21, m22):
    return m11 * m22 - m12 * m21

def mat2_inverse(m11, m12, m21, m22):
    det = mat2_det(m11, m12, m21, m22)
    scale = 1.0 / det
    n11 = scale * m22
    n12 = - scale * m12
    n21 = - scale * m21
    n22 = scale * m11
    return n11, n12, n21, n22

def mat2_vec2_mul(m11, m12, m21, m22, v1, v2) -> tuple[float, float]:
    r1 = m11 * v1 + m12 * v2
    r2 = m21 * v1 + m22 * v2

    return r1, r2

total_tokens = 0

for machine in claw_machines:

    m11 = machine.a.x
    m12 = machine.b.x
    m21 = machine.a.y
    m22 = machine.b.y

    b1 = machine.goal.x
    b2 = machine.goal.y

    n11, n12, n21, n22 = mat2_inverse(m11,m12,m21,m22)
    x1, x2 = mat2_vec2_mul(n11, n12, n21, n22, b1, b2)

    if round(x1,3).is_integer() and round(x2,3).is_integer():
        a_tokens = int(round(x1,3))
        b_tokens = int(round(x2,3))

        total_tokens += BUTTON_TOKENS_A * a_tokens + BUTTON_TOKENS_B * b_tokens

print("Total tokens", total_tokens)

