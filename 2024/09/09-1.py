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

SIZE = len(data)

def print_matrix(matrix):
    for row in range(len(matrix)):
        for col in range(len(matrix)):
            print(matrix[row][col], end="")
        print()

# Problem solution

def representation(s):
    viz = []
    for i, c in enumerate(s):
        size = int(c)
        is_file = i % 2 == 0
        
        if is_file:
            id = i // 2
            viz += [id] * size
        else:
            viz += ["."] * size

    return viz


def move_front_cursor(cursor, data):
    for i in range(cursor, len(data)):
        if data[i] == ".":
            return i
    raise Exception("Front cursor of out bounds")

def move_back_cursor(cursor, data):
    for i in reversed(range(cursor)):
        if data[i] != ".":
            return i
    raise Exception("Back cursor of out bounds")

def checksum(s):
    chsum = 0
    for i,c in enumerate(s):
        if c == ".":
            continue # break I guess?
        chsum += i*int(c)
    return chsum

def showrepr(data):
    return "".join(map(str, data))

data = data[0]
if not is_test:
    print(data)

current = representation(data)

MAX_ITER = 50000
iterations = 0

spaces = current.count(".")

print("Spaces", spaces, "Length", len(current))

front_cursor = move_front_cursor(0, current)
back_cursor = move_back_cursor(len(current), current)

if not is_test:
    print("Initial", showrepr(current), front_cursor, back_cursor)

while front_cursor < back_cursor:
    
    current[front_cursor] = current[back_cursor]
    current[back_cursor] = "."

    front_cursor = move_front_cursor(front_cursor, current)
    back_cursor = move_back_cursor(back_cursor, current)

    iterations += 1
    if iterations == MAX_ITER:
        print("MAX ITERATIONS REACHED")
        break
    if not is_test:
        print(showrepr(current), front_cursor, back_cursor)

# print("Done", current)
print("Iterations", iterations)
print("Checksum", checksum(current))