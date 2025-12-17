from collections import deque
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
tree: dict[str, list[str]] = {"out": []}
for d in data:
    source, outputs = d.split(":")
    outputs = outputs.strip().split(" ")
    print(source, outputs)
    tree[source] = outputs


def number_of_paths(node, target, has_fft, has_dac, cache):
    if (node, has_fft, has_dac) in cache:
        print("Cache hit")
        return cache[(node, has_fft, has_dac)]
    
    if node == target:
        return 1 if has_dac and has_fft else 0
    
    has_fft = has_fft | (node == "fft")
    has_dac = has_dac | (node == "dac")
    result = 0
 
    for next in tree[node]:
        result += number_of_paths(next, target, has_fft, has_dac, cache)
    
    cache[(node, has_fft, has_dac)] = result
    return result

cache = {}
score = number_of_paths("svr", "out", False, False, cache)
print(cache)

# score = 0
print(f"{score=}")
