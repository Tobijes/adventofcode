# Load data

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
            print(matrix[row][col], end="")
        print()

# Problem solution
A = int(data[0].split(" ")[-1])
B = int(data[1].split(" ")[-1])
C = int(data[2].split(" ")[-1])

program = [int(opcode) for opcode in data[-1].split(" ")[-1].split(",")]

inst_ptr = 0

def combo(operand):
    if operand >= 0 and operand <= 3:
        return operand
    if operand == 4:
        return A
    if operand == 5:
        return B
    if operand == 6:
        return C
    
print(A,B,C,program)

out = []
PLEN = len(program)

while inst_ptr < PLEN:

    opcode = program[inst_ptr]

    if opcode == 3: #jnz
        if A == 0:
            print(f"{inst_ptr=} {opcode=} no jump {A=} {B=} {C=}")
            inst_ptr += 1
        else: 
            operand = program[inst_ptr+1]
            print(f"{inst_ptr=} {opcode=} {operand=} {A=} {B=} {C=}")
            inst_ptr = operand
        continue
    
    if inst_ptr+1 >= PLEN:
        break
    operand = program[inst_ptr+1]
    print(f"{inst_ptr=} {opcode=} {operand=} {A=} {B=} {C=}")

    if opcode == 0: #adv
        numerator = A
        denominator = 2**combo(operand)
        A = int(numerator / denominator)
    elif opcode == 1: #bxl
        B = B ^ operand
    elif opcode == 2: #bst
        B = (combo(operand) % 8) & 0b111
    # Skip opcode 3 (top)
    elif opcode == 4: #bxc
        B = B ^ C
    elif opcode == 5: #out
        out.append(combo(operand) % 8)
    elif opcode == 6: #bdv
        numerator = A
        denominator = 2**combo(operand)
        B = int(numerator / denominator)
    elif opcode == 7: #cdv
        numerator = A
        denominator = 2**combo(operand)
        C = int(numerator / denominator)
    else:
        raise Exception("Unknown opcode")
    inst_ptr += 2

print("Output:")
print(",".join(map(str,out)))