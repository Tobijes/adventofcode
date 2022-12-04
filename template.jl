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

