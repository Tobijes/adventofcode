# Load data

import sys
from dataclasses import dataclass
import re

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
class Machine:
    light_pattern_str: str 
    button_masks: list[int]
    joltages: list[int]

def binarypos(k:int, l:int):
    a = ['0'] * l
    a[k] = '1'
    
    return int("0b" + "".join(a),2)

def print_machine(m: Machine):
    print(f"Light: {m.light_pattern_str}", end=" | Buttons: ")

    for b in m.button_masks:
        s = f"{b:b}".zfill(len(m.light_pattern_str))
        print(s, end=" ")
    
    print("")

machines: list[Machine] = []

for d in data:
    # printl(d)
    (m := re.match(r"\[(.+)\] (.*) \{(.+)\}", d))
    groups = m.groups()
    # light
    light_pattern_str = groups[0].replace('.','0').replace('#','1')
    L = len(light_pattern_str)
    # button
    buttons = [list(map(int,g.split(","))) for g in groups[1].replace('(','').replace(')','').split()]
    button_masks = [sum([binarypos(k,L) for k in button]) for button in buttons]

    # joltages
    joltages = groups[2] 
    machines.append(Machine(
        light_pattern_str=light_pattern_str,
        button_masks=button_masks,
        joltages=[]
    ))

for m in machines:
    print_machine(m)

def toggle(pattern: tuple[bool], indexes:list[int]):
    lst = list(pattern)
    for i in indexes:
        lst[i] = not pattern[i]
    return tuple(lst)

# cache = dict()

# def find_match(pattern: tuple[bool], presses: int, machine: Machine):
#     if pattern in cache and presses > cache[pattern]:
#         return cache[pattern]
    
#     if presses > 100:
#         return presses
    
#     if pattern == machine.light_pattern:
#         # print("Match!")
#         return presses
    
#     results = []
#     for button_idxs in machine.buttons:
#         new_pattern = toggle(pattern, button_idxs)
#         # print(pattern, button_idxs, new_pattern)
#         new_presses = find_match(new_pattern, presses+1, machine)

#         results.append(new_presses)
    
#     min_presses = min(results)

#     if pattern not in cache:
#         cache[pattern] = min_presses
#     cache[pattern] = min(cache[pattern], min_presses)
#     return min_presses

# score = 0
# for i, m in enumerate(machines):
#     cache = {}
#     pattern = tuple([False] * len(m.light_pattern))
#     presses = find_match(pattern, 0, m)
#     print(f"{i+1}/{len(machines)} {presses=}")
#     score += presses

# print(f"{score=}")