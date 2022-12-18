using Test

function work(filepath::String)
    f = open(filepath)


    for l in eachline(f)

    end

    close(f)

    0
end
result = work("15/sample.txt")
#result = work("15/input.txt")
println("Result: ", result)
@test result == 26 skip=true
