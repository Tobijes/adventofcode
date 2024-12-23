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

def print_game(game):
    for row in range(SIZE):
        for col in range(SIZE):
            print(game[row][col], end="")
        print("")



# Return is loop or not
def run_game(game, start_pos, start_dir, obstacle_pos=None):
    if obstacle_pos:
        obstacle_row, obstacle_col = obstacle_pos
        game[obstacle_row][obstacle_col] = "O"
    # print_game(game)
    cur_row, cur_col = start_pos
    cur_dir = start_dir
    history = {}
    for i in range(50000): # Capped while-loop

        # Mark visited
        game[cur_row][cur_col] = cur_dir # For visual

        if (cur_row, cur_col) in history:
            history[(cur_row, cur_col)].append(cur_dir)
        else:
            history[(cur_row, cur_col)] = [cur_dir]

        dir_row, dir_col = directions[cur_dir]
        next_row = cur_row + dir_row
        next_col = cur_col + dir_col
        
        if not within(next_row, next_col):
            # Guard left
            return False, game

        if game[next_row][next_col] in "#O":
            cur_dir = rotation[cur_dir]
            continue

        cur_row = next_row
        cur_col = next_col

        if (cur_row,cur_col) in history and cur_dir in history[(cur_row,cur_col)]:
            # Loop found
            return True, game
    
    print("MAX ITERS!")
    print_game(game)
    return False, game


for row in range(SIZE):
    for col in range(SIZE):
        if game[row][col] in directions:
            start_row = row
            start_col = col
            start_dir = game[row][col]

game_copy = [x[:] for x in game]
_, original_game = run_game(game_copy, (start_row, start_col), start_dir)
print_game(original_game)
candidates = []
for row in range(SIZE):
    for col in range(SIZE):
        if original_game[row][col] in directions:
            candidates.append((row,col))

print(candidates)
print(len(candidates))

result = 0
for row,col in candidates:
        # print(row,col)
        # print_game(game)
        game_copy = [x[:] for x in game]
        # print("")
        # print_game(game_copy)
        loop, _ = run_game(game_copy, (start_row, start_col), start_dir, (row,col))
        result += loop

print("Result", result)