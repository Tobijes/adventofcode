# Load data

import sys
import math

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
        
data = [l.rstrip('\n') for l in data]

def print_matrix(matrix):
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            print(matrix[row][col], end="")
        print()

# Problem solution
def signindex(row: list, cursor):
    try:
        addition = row.index('+', cursor)
    except Exception as e:
        # print('+', e)
        addition = None

    try:
        multiplication = row.index('*', cursor)
    except Exception as e:
        # print('*', e)
        multiplication = None
        
    if addition is None and multiplication is None:
        return None
    if addition is None:
        return multiplication
    if multiplication is None:
        return addition
    
    return min(addition, multiplication)

def vstrip(slice):
    for col in range(len(slice[0])):
        s = ''
        for row in range(len(slice)):
            s += slice[row][col]
        s = s.strip()
        if s != '':
            yield int(s)

width = len(data[0])
print(data[-1])
cursor = 0
score = 0
while cursor != None:
    start_index = signindex(data[-1], cursor)
    end_index = signindex(data[-1], cursor+1)

    print(start_index,end_index)
    sign = data[-1][start_index]
    if end_index is None:
        slice = [row[start_index:] for row in data[:-1]]
    else:
        slice = [row[start_index:end_index] for row in data[:-1]]
    print(sign, slice)

    numbers = list(vstrip(slice))
    print(numbers)

    if sign == '+':
        score += sum(numbers)
    else:
        score += math.prod(numbers)

    cursor = end_index 

print("Score", score)
