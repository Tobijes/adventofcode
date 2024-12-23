# Load data

import sys

if len(sys.argv) > 1 and sys.argv[1] == "t":
    with open("input.txt") as f:
        data =  f.readlines()
else:
    with open("sample.txt") as f:
        data =  f.readlines()

SIZE = len(data)
# Problem solution
directions = {
    "^" : (-1, 0),
    ">" : (0, 1),
    "v" : (1, 0),
    "<": (0, -1)
}

rotation = {
    "^" : ">",
    ">" : "v",
    "v" : "<",
    "<": "^"
}

game = data
for i in range(SIZE):
    game[i] = list(game[i])

# Naive search
def within(cur_row, cur_col):
    return cur_row >= 0 and cur_row < SIZE and cur_col >= 0 and cur_col < SIZE

def print_game():
    for row in range(SIZE):
        for col in range(SIZE):
            print(game[row][col], end="")
        print("")

print_game()
for row in range(SIZE):
    for col in range(SIZE):
        if game[row][col] in directions:
            cur_row = row
            cur_col = col
            cur_dir = game[row][col]

while within(cur_row, cur_col):
    # Mark visited
    game[cur_row][cur_col] = "X"
    
    dir_row, dir_col = directions[cur_dir]
    next_row = cur_row + dir_row
    next_col = cur_col + dir_col
    
    if within(next_row, next_col) and game[next_row][next_col] == "#":
        cur_dir = rotation[cur_dir]
        continue

    cur_row = next_row
    cur_col = next_col
print()
print_game()
    
result = 0

for row in range(SIZE):
    for col in range(SIZE):
        if game[row][col] == 'X':
            result += 1

print("Result", result)