using Test

function evaluate(line::String)
        
    0
end

function work(filepath::String)
    f = open(filepath)

    mySum = 0
    for l in eachline(f)
        result = evaluate(l)
        mySum += result
    end

    close(f)

    mySum
end

result = work("13/sample.txt")
#result = work("13/input.txt")
println("Result: ", result)
@test result == 13 skip=true
