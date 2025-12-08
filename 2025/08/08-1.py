# Load data
import math
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
            print(int(matrix[row][col]), end=" ")
        print()

# Problem solution
def dist(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2 + (p1[2] - p2[2])**2)

def findmin(data: list[list[float]], blacklist: set[tuple[int,int]]):
    min_value = 1000000
    min_i = None
    min_j = None

    for i in range(len(data)):
        for j in range(i+1, len(data)):
            if (i,j) in blacklist:
                continue
            if data[i][j] < min_value:
                min_value = data[i][j]
                min_i = i
                min_j = j
    return min_value, min_i, min_j


data = [tuple(int(x) for x in d.split(",")) for d in data]

distances = [[dist(data[i],data[j]) for i in range(len(data))] for j in range(len(data))]
# print(data)
# print_matrix(distances)
# print("")


# List of circuits which are sets of data index
circuits: list[set[int]] = []
blacklist: set[tuple[int, int]] = set()

rounds = 1000 if is_test else 10
for n in range(rounds):
    min_value, i, j = findmin(distances, blacklist)
    connectors: list[int] = []
    for k, circuit in enumerate(circuits):
        if i in circuit or j in circuit:
            connectors.append(k)
    
    if len(connectors) == 0:
        circuits.append(set([i,j]))
    elif len(connectors) == 1:
        k = connectors[0]
        circuits[k].add(i)
        circuits[k].add(j)
    else:
        k1 = connectors[0]
        set1 = circuits[connectors[0]] 
        set2 = circuits[connectors[1]]
        circuits.remove(set1)
        circuits.remove(set2)
        circuits.append(set.union(set1, set2))

    blacklist.add((i,j))
    # print(f"{blacklist=} {circuits=}")
    print(n)

circuit_lens = [len(c) for c in circuits]
circuit_lens.sort(reverse=True)
print(circuit_lens[:3])
print("Score:", math.prod(circuit_lens[:3]))