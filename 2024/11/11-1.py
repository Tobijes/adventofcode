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
stones =  [stone for stone in data[0].split()]
def blink(stone):

    if int(stone) == 0:
        return "1", None
    
    if len(stone) % 2 == 0:
        mid = len(stone) // 2

        s1 = str(int(stone[:mid]))
        s2 = str(int(stone[mid:]))

        return s1, s2
    
    return str(int(stone) * 2024), None

# def blink(stone):

#     if stone[0] == 0:
#         return (1, "1"), None
    
#     if len(stone[1]) % 2 == 0:
#         mid = len(stone[1]) // 2

#         s1_st = stone[1][:mid]
#         s1_int = int(s1_st)
#         s1_st = str(s1_int)

#         s2_st = stone[1][mid:]
#         s2_int = int(s2_st)
#         s2_st = str(s2_int)

#         return (s1_int, s1_st), (s2_int, s2_st)
    
#     s_int = stone[0] * 2024
#     s_str = str(s_int)
#     return (s_int, s_str), None

print("Initial", stones)
for i in range(25):
    new_stones = []
    for stone in stones:
        s1, s2 = blink(stone)
        new_stones.append(s1)

        if s2 is not None:
            new_stones.append(s2)

    stones = new_stones
    print(str(i+1)+"th blink", len(stones))

