# Load data

import sys

with open("input.txt") as f:
    file_input = f.read()

with open("sample2.txt") as f:
    file_sample = f.read()

data = file_sample

if len(sys.argv) > 1 and sys.argv[1] == "t":
    data = file_input

# Problem solution
import re
p = re.compile(r"mul\((\d\d?\d?),(\d\d?\d?)\)|(don\'t\(\))|(do\(\))")

s = 0
enable = True
for m in p.finditer(data):
    print(m.group())
    print(m.groups())
    a, b, dont, do = m.groups()
    if dont is not None:
        enable = False
        
    if do is not None:
        enable = True

    if a is not None and b is not None and enable:
        s += int(a) * int(b)

print(s)