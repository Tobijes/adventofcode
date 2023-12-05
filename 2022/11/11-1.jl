using Test
using Match

mutable struct Monkey
    num::Int64
    items::Array{Int64, 1}
    operand1
    operation::String
    operand2
    testDivisor::Int64
    throwTrue::Int64
    throwFalse::Int64
    inspection::Int64
end

function work(filepath::String)
    f = open(filepath)

    monkeys = []

    # Parse input data
    curMonkeyIdx = 0
    lineParseIdx = 0
    for l in eachline(f)
        l = strip(l)
        if lineParseIdx  == 0
            m = match(r"Monkey (\d+):", l)
            # println(m[1])
            num = parse(Int64, m[1])
            curMonkeyIdx = num+1
            push!(monkeys, Monkey(num, [], 0, "+", 0, 0, 0, 0, 0))
        elseif lineParseIdx == 1
            for m in eachmatch(r"(\d+)", l)
                num = parse(Int64, m[1])
                push!(monkeys[curMonkeyIdx].items, num)
            end
        elseif lineParseIdx == 2 # Operation
            parts = split(l)
            monkeys[curMonkeyIdx].operand1 = parts[end-2]
            monkeys[curMonkeyIdx].operation = parts[end-1]
            monkeys[curMonkeyIdx].operand2 = parts[end]
        elseif lineParseIdx == 3 # Test, divisor
            parts = split(l)
            monkeys[curMonkeyIdx].testDivisor = parse(Int64, parts[end])
        elseif lineParseIdx == 4 # True test
            parts = split(l)
            monkeys[curMonkeyIdx].throwTrue = parse(Int64, parts[end])
        elseif lineParseIdx == 5 # False test
            parts = split(l)
            monkeys[curMonkeyIdx].throwFalse = parse(Int64, parts[end])
        end
        
        lineParseIdx += 1
        if lineParseIdx > 6
            lineParseIdx = 0
        end
    end

    close(f)
    println(monkeys)

    # Run
    for round in 1:20

        for monkey in monkeys
            # if length(monkey.items) > 0
            #     monkey.inspection += 1
            # end
            foreach(monkey.items) do item
                worry = 0
                a = monkey.operand1 == "old" ? item : parse(Int64, monkey.operand1);
                b = monkey.operand2 == "old" ? item : parse(Int64, monkey.operand2);
                worry = monkey.operation == "*" ? a * b : a + b
                worry = floor(Int64, worry / 3)
                # println(worry)
                monkey.inspection += 1
                if worry % monkey.testDivisor == 0
                    push!(monkeys[monkey.throwTrue + 1].items, worry)
                else
                    push!(monkeys[monkey.throwFalse + 1].items, worry)
                end
            end
            monkey.items = []
        end

    end

    println(monkeys)

    result = map(monkeys) do monkey
        (monkey.num, monkey.inspection)
    end

    println(result)
    sorted = sort(map(x->x[2], result), rev=true)
    sorted[1] * sorted[2]
end

result = work("11/sample.txt")
# result = work("11/input.txt")
println("Result: ", result)
@test result == 10605
