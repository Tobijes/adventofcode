using Test

function uniqueWindow(arr) 
    length(Set(arr)) == 14
end

function evaluate(line::String)
    println(line)
    signal = split(line, "")
    
    window = signal[1:14]
    # base case
    if uniqueWindow(window)
        return 14
    end

    # continous case
    for i in 15:length(signal)
        popfirst!(window)
        push!(window, signal[i])
        if uniqueWindow(window)
            return i
        end
    end

    0
end

function work(filepath::String)
    f = open(filepath)

    line = first(eachline(f))
    
    close(f)

    evaluate(line)
end

# result = work("06/sample.txt")
result = work("06/input.txt")
println("Result: ", result)
# @test result == 19
