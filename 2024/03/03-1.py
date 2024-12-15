# Load data

import sys

with open("input.txt") as f:
    file_input = f.read()

with open("sample.txt") as f:
    file_sample = f.read()

data = file_sample

if len(sys.argv) > 1 and sys.argv[1] == "t":
    data = file_input

# Problem solution
import re
p = re.compile(r"mul\((\d\d?\d?),(\d\d?\d?)\)")

s = 0
for m in p.finditer(data):
    print(m.groups())
    a, b = m.groups()
    s += int(a) * int(b)

print(s)