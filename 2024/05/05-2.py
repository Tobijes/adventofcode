from functools import cmp_to_key
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
rules, updates = data.split("\n\n")
rules = rules.split("\n")
updates = updates.split("\n")
updates = list(map(lambda x : x.split(","), updates))

print(rules)
all = set()
for rule in rules:
    before, after = rule.split("|")
    all.add(before)
    all.add(after)

x_before = {x: [] for x in all}
x_after = {x: [] for x in all}

for rule in rules:
    before, after = rule.split("|")
    x_before[before].append(after)
    x_after[after].append(before)
    

print(all)
print(x_before)
print(x_after)

print(updates)


def validate_update(update):
    # print(update)
    for i in range(len(update)):
        for j in range(len(update)):
            if i == j: # skip self
                continue

            ival = update[i]
            jval = update[j]
            if j < i and (jval in x_before[ival] or ival in x_after[jval]):
                # print("Not valid. Condition 1")
                # print(i, j, ival, jval, x_after[ival], x_before[jval])
                return False
            if j > i and (jval in x_after[ival] or ival in x_before[jval]):
                # print("Not valid. Condition 2")
                # print(i, j, ival, jval, x_before[ival], x_after[jval])
                return False
            
    return True

def compare(a,b):
    if a in x_before[b]:
        return 1
    elif a in x_after[b]:
        return -1
    else: 
        return 0

result = 0
for update in updates:
    if validate_update(update):
        continue
    
    print(update)
    ordered = sorted(update, key=cmp_to_key(compare))
    print(f"{ordered=}")

    result += int(ordered[len(ordered) // 2])

print(result)


        
