import itertools
# Load data

import sys

if len(sys.argv) > 1 and sys.argv[1] == "t":
    with open("input.txt") as f:
        data =  f.readlines()
else:
    with open("sample.txt") as f:
        data =  f.readlines()

SIZE = len(data)

equations = []
for line in data:
    test_value, values = line.split(":")
    test_value = int(test_value)
    values = [int(s) for s in values.split()]
    print(test_value, values)
    equations.append((test_value, values))

def evaluate(values, operators):
    rolling = values[0]
    for i in range(0, len(operators)):
        operator = operators[i]
        if operator == '+':
            rolling += values[i+1]
        elif operator == '*':
            rolling *= values[i+1]
        elif operator == '||':
            rolling = int(str(rolling)+str(values[i+1]))
        else:
            raise Exception("Unknown operator")
    return rolling

def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

result = 0
for test_value, values in equations:
    spots = list(range(len(values)-1))
    candidates = list(itertools.product(*([['*', '+', '||']] * len(spots))))
    for candidate in candidates:
        evaluation = evaluate(values, candidate)
        # print(test_value, values, candidate, evaluation)
        if evaluation == test_value:
            result += test_value
            break


print(f"{result=}")