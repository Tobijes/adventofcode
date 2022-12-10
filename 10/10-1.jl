using Test

function evaluate(line::String)
        
    0
end

function work(filepath::String)
    f = open(filepath)

    X = 1
    cycle = 0
    values = []

    check() = begin
        if cycle == 20 || (cycle -20) % 40 == 0
            println((cycle, X, X*cycle))
            push!(values, X * cycle)
        end
    end

    for l in eachline(f)
        if l == "noop"
            cycle += 1
            check()
            continue
        end

        (op, num) = split(l, " ")

        cycle += 1
        check()

        cycle += 1
        check()
        X += parse(Int64, num)

    end

    close(f)
    sum(values)
end

# result = work("10/sample.txt")
result = work("10/input.txt")
println("Result: ", result)
# @test result == 13140