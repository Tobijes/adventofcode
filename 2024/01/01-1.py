with open("input.txt") as f:
    file_input = f.read()

with open("sample.txt") as f:
    file_sample = f.read()


data = file_input
lines = data.split("\n")

left = []
right = []

for line in lines:
    a, b = line.split()
    left.append(int(a))
    right.append(int(b))

print(left, right)

left.sort()
right.sort()

distances = 0

for a,b in zip(left,right):
    distances += abs(a-b)

print(distances)