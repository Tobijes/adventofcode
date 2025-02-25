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

if not is_test:
    print(data)

def print_matrix(matrix):
    for row in range(len(matrix)):
        for col in range(len(matrix)):
            print(matrix[row][col], end="")
        print()

# Problem solution
# stones: list[tuple[int, str]] = [(int(stone), stone) for stone in data[0].split()]
initial_stones =  [stone for stone in data[0].split()]

CACHE = {}

def blink_recursive_cache(stone, depth_left):
    if depth_left == 0:
        return 1 
    
    ch_idx = (stone,depth_left)

    if ch_idx in CACHE:
        return CACHE[ch_idx]

    if stone == "0":
        result = blink_recursive_cache("1", depth_left-1)
    
    elif len(stone) % 2 == 0:
        mid = len(stone) // 2

        s1 = str(int(stone[:mid]))
        s2 = str(int(stone[mid:]))

        r1 = blink_recursive_cache(s1, depth_left-1)
        r2 = blink_recursive_cache(s2, depth_left-1)

        result =  r1 + r2
    else:
        s = str(int(stone) * 2024)
        result = blink_recursive_cache(s, depth_left-1)

    CACHE[ch_idx] = result

    return result

NUM_BLINKS = 75
print("Initial", initial_stones)
stone_sum = 0
for stone in initial_stones:
    stone_sum += blink_recursive_cache(stone, depth_left=NUM_BLINKS)
   
print("Num stones", stone_sum)
