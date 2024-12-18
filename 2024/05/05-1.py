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

result = 0
for update in updates:
    valid = True
    print(update)
    for i in range(len(update)):
        if not valid:
            break
        for j in range(len(update)):
            if i == j: # skip self
                continue

            ival = update[i]
            jval = update[j]
            if j < i and (jval in x_before[ival] or ival in x_after[jval]):
                valid = False
                print("Not valid. Condition 1")
                print(i, j, ival, jval, x_after[ival], x_before[jval])
                break
            if j > i and (jval in x_after[ival] or ival in x_before[jval]):
                valid = False
                print("Not valid. Condition 2")
                print(i, j, ival, jval, x_before[ival], x_after[jval])
                break
            
    if not valid:
        continue

    result += int(update[len(update) // 2])

        
print(result)