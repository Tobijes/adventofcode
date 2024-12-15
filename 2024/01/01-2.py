import sys

with open("input.txt") as f:
    file_input = f.read()

with open("sample.txt") as f:
    file_sample = f.read()

data = file_sample

if len(sys.argv) > 1 and sys.argv[1] == "t":
    data = file_input

lines = data.split("\n")

left = []
right = []

for line in lines:
    l, r = line.split()
    left.append(int(l))
    right.append(int(r))

print(left, right)

lookup = {}
for r in right:
    if r in lookup:
        lookup[r] += 1
    else:
        lookup[r] = 1

print(lookup)

similarity = 0

for l in left:
    if l in lookup:
        similarity += l * lookup[l]

print(similarity)