import re

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
def num2bnum(nb: int, length: int) -> int:
    s = ['0'] * length
    for n in nb:
        s[n] = '1'
    s = "".join(s)
    return s

def parse_machine(line: str):
    light = line[line.index('[')+1:line.index(']')]
    light = ['1' if c == '#' else '0' for c in light]
    light = "".join(light)
    buttons_strip = line[line.index('('):line.index('{')-1]
    buttons_strip = buttons_strip.replace('(', '').replace(')','')
    buttons_strs  = buttons_strip.split(" ")
    buttons_strs = [list(map(int, bs.split(","))) for bs in buttons_strs]
    button_masks = [num2bnum(but, len(light)) for but in buttons_strs]
    return light,  button_masks

def find_button_presses(target, buttons):

    filtermax = 2**len(buttons)
    filterwidth = len(bin(filtermax)[2:]) - 1
    # print(f"{filtermax=:b}")
    solutions = []
    for i in range(filtermax):
        binary_str = bin(i)[2:].zfill(filterwidth)
        # print(binary_str)
        current = 0
        for i, b in enumerate(binary_str):
            if b == '1':
                current ^= buttons[i]

        if current == target:
            solutions.append(binary_str)

    return solutions

score = 0
for d in data:
    target_str, button_strs = parse_machine(d)
    print(button_strs, button_strs)

    target = int(target_str, 2)
    buttons = [int(bs, 2) for bs in button_strs]

    solutions = find_button_presses(target, buttons)
    print(f"{solutions=}")
    solution_presses = [sum([1 if c == '1' else 0 for c in sol]) for sol in solutions]
    score += min(solution_presses)

print(f"{score=}")

