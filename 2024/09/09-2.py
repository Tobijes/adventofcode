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
    id = None
    file_start = None
    file_end = None
    for i in reversed(range(cursor)):
        if id is None: # Where are looking for a file id
            if data[i] != ".":
                id = data[i]
                file_start = i
                file_end = i
            else:
                continue
        else: # We have a open file
            if data[i] != id:
                break
            else:
                file_start = i
    return (id, file_start, file_end)

def find_file(data: list, id, start=0, stop=sys.maxsize):
    file_start = data.index(id,start,stop)
    file_end = file_start
    for i in range(file_start, len(data)):
        if data[i] != id:
            break
        file_end = i
    return file_start, file_end

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

current = []
num_files = 0
for i, c in enumerate(data):
    size = int(c)
    is_file = i % 2 == 0
    
    if is_file:
        id = i // 2
        current += [id] * size
        num_files += 1
    else:
        current += ["."] * size


MAX_ITER = 50000
iterations = 0

spaces = current.count(".")


spaces= []

cur_start = None
cur_size = 0
for i, c in enumerate(current):
    if cur_start is None:
        if c == ".":
            cur_start = i
            cur_size = 1
        else:
            continue
    else:
        if c == ".":
            cur_size += 1
        else:
            spaces.append((cur_start, cur_size))
            cur_start = None
            cur_size = 0

if not is_test:
    print("Initial", showrepr(current), spaces)

for id in reversed(range(num_files)):
    file_start, file_end = find_file(current, id)
    file_len = file_end - file_start + 1
    
    if not is_test:
        print(id, file_start, file_end, file_len)

    space_index = None
    for i, (start, size) in enumerate(spaces):
        if size >= file_len and start < file_start: 
            space_index = i
            break

    if space_index is None:
        if not is_test:
            print(id, "no space available")
        continue
    
    space_start, space_size = spaces[space_index]
    for i in range(space_start, space_start + file_len):
        current[i] = id
    
    for i in range(file_start, file_end+1):
        current[i] = "."
 
    spaces[space_index] = (space_start+file_len, space_size - file_len)
    if spaces[space_index][1] == 0:
        del spaces[space_index]

    if not is_test:
        print(showrepr(current), spaces)


# while front_cursor < back_cursor:
    
#     current[front_cursor] = current[back_cursor]
#     current[back_cursor] = "."

#     front_cursor = move_front_cursor(front_cursor, current)
#     back_cursor = move_back_cursor(back_cursor, current)

#     iterations += 1
#     if iterations == MAX_ITER:
#         print("MAX ITERATIONS REACHED")
#         break
#     if not is_test:
#         print(showrepr(current), front_cursor, back_cursor)

if not is_test:
    print(showrepr(current))
print("Done")
print("Iterations", iterations)
print("Checksum", checksum(current))