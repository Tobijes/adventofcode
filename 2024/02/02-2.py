import sys

with open("input.txt") as f:
    file_input = f.read()

with open("sample.txt") as f:
    file_sample = f.read()

data = file_sample

if len(sys.argv) > 1 and sys.argv[1] == "t":
    data = file_input


reports = data.split("\n")
reports = [[int(value) for value in levels.split()] for levels in reports ]
print(reports)

def diff_filter(lst):
    for i in range(len(lst)-1):
        yield lst[i] - lst[i+1]

safe_count = 0
for levels_full in reports:
    # Brute force method
    for i in range(len(levels_full)):
        levels = levels_full[:i] + levels_full[i+1:]

        diffs = list(diff_filter(levels))
        print(diffs)
        distances = [abs(d) for d in diffs]
        if max(distances) > 3 or min(distances) < 1:
            print("Not safe")
            continue # Not safe
        
        # As min distance is now 1, we can look at sign
        signs = [1 if d > 0 else -1 for d in diffs]
        if len(set(signs)) > 1:
            print("Not safe")
            continue # More than one sign

        print("Safe")
        safe_count += 1
        break

print(safe_count)