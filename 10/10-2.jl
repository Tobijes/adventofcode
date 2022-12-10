using Test

function evaluate(line::String)
        
    0
end

function work(filepath::String)
    f = open(filepath)

    X = 1
    cycle = 0

    render() = begin
        pos = cycle % 40
        if X - 1 <= pos <= X + 1
            # println(("#", cycle, pos,X))  
            print("#")
        else
            # println((".", cycle, pos,X))  
            print(".")
        end
        if cycle % 40 == 0
            println(cycle)
        end
    end
    for l in eachline(f)
        if l == "noop"
            cycle += 1
            render()
        else
            (_, num) = split(l, " ")
            
            cycle += 1
            render()

            cycle += 1
            render()

            X += parse(Int64, num)
        end
    end
    println()
    close(f)
    0
end

result = work("10/sample.txt")
# result = work("10/input.txt")
println("Result: ", result)
# @test result == 13140