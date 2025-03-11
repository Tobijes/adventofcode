import queue

def run(A, B, C):
    B = A % 8

    B = B ^ 0b11

    C = A >> B

    A = A >> 3

    B = B ^ 0b101

    B = B ^ C

    out = B % 8
    return out

programme = list(reversed([2,4,1,3,7,5,0,3,1,5,4,4,5,5,3,0]))
# programme = [0,3,5,5,4,4,5,1,3,0,5,7,3,1,4,2]

Bitstring = int
Program = list[int]
candidates: queue.Queue[tuple[Bitstring, Program]] = queue.Queue()
solutions: list[Bitstring] = []

candidates.put((0, programme))

while not candidates.empty():
    bits, program = candidates.get()
    O = program[0]

    for A in range(0b1000):
        newfull = bits << 3 | A
        out = run(newfull,0,0)
        
        print(f"{O=}/{O:b}, {A=}/{A:b} -> {newfull=}/{newfull:b} = {out=}/{out:b}")

        if out == O:
            print(f"Pick {A=}/{A:b}")
           
            if len(program) == 1:
                solutions.append(newfull)
            else:
                candidates.put((newfull, program[1:]))

for solution in solutions:
    print(f"{solution=}/{solution:b}")

min_solution = min(solutions)
print(f"{min_solution=}/{min_solution:b}")