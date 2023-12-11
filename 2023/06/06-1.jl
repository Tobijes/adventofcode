using Test

function work(filepath::String)
    f = open(filepath)


    for l in eachline(f)

    end

    close(f)

    0
end
result = work("06/sample.txt")
#result = work("06/input.txt")
println("Result: ", result)
