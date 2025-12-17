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
tree: dict[str, list[str]] = {}
for d in data:
    source, outputs = d.split(":")
    outputs = outputs.strip().split(" ")
    print(source, outputs)
    tree[source] = outputs

print(tree)
q = deque()
q.append(["you"])

paths = []

while len(q) > 0:
    e = q.popleft()
    last = e[-1]
    for output in tree[last]:
        nextpath = e + [output]
        if output == "out":
            paths.append(nextpath)
        else:
            q.append(nextpath)

score = len(paths)
print(f"{score=}")
