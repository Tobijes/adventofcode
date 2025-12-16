import sys
from scipy.optimize import linprog

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
def parse_machine(line: str):
    light = line[line.index('[')+1:line.index(']')]
    light = ['1' if c == '#' else '0' for c in light]
    light = "".join(light)
    
    buttons_strip = line[line.index('('):line.index('{')-1]
    buttons_strip = buttons_strip.replace('(', '').replace(')','')
    buttons_strs  = buttons_strip.split(" ")
    buttons = [set(map(int, bs.split(","))) for bs in buttons_strs]
    # button_masks = [num2bnum(but, len(light)) for but in buttons_strs]

    joltages = line[line.index('{')+1:line.index('}')]
    joltages = joltages.split(",")
    joltages = list(map(int, joltages))

    return buttons, joltages

score = 0
for d in data:
    buttons, joltages = parse_machine(d)
    print(buttons, joltages)
    
    constraints = [[0] * len(buttons) for _ in range(len(joltages))]

    for i in range(len(joltages)):
        for j in range(len(buttons)):
            button = buttons[j]
            if i in button:
                constraints[i][j] = 1
  
    print_matrix(constraints)
    c = [1] * len(buttons)

    result = linprog(c=c, A_eq=constraints, b_eq=joltages, integrality=1, bounds=[(0, None)] * len(buttons))
    fewest = result.fun
    score += fewest
    solution = list(map(int, result.x))
    print(fewest, solution)

print(f"{score=}")

# #

# 0*x0 + 0*x1 + 0*x2 + 0*x3 + 1*x4 + 1*x5 = 3
# 0*x0 + 1*x1 + 0*x2 + 0*x3 + 0*x4 + 1*x5 = 5
# 0*x0 + 0*x1 + 1*x2 + 1*x3 + 1*x4 + 0*x5 = 4
# 1*x0 + 1*x1 + 0*x2 + 1*x3 + 0*x4 + 0*x5 = 7


# x_1=2+x_6
# x_2=5-x_6
# x_3=1-x_4+x_6
# x_4=x_4
# x_5=3-x_6
# x_6=x_6

# x1=1
# x2=3
# x4=3
# x5=1
# x6=2
