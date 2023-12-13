using Test

DEBUG = true

function debug(args...)
    if DEBUG
        println(args...)
    end
end

function cleansplit(s::AbstractString, sep::String)
    splitted = split(s, sep, keepempty=false)
    map(x->strip(x), splitted)
end

function diff(array)
    result = zeros(length(array) - 1)
    for i in 1:length(array)-1
        result[i] = array[i+1] - array[i]
    end
    return result
end

# function extrapolate(left, below)
#     push
# end

function work(filepath::String)
    f = open(filepath)

    s = 0
    for l in eachline(f)
        histories = []
        history = parse.(Int, cleansplit(l, " "))
        push!(histories, history)
        while any(history .!= 0)
            history = diff(history)
            push!(histories, history)
        end
        for history in histories
            debug(history)
        end

        for i in length(histories)-1:-1:1
            push!(histories[i], histories[i][end] + histories[i+1][end]) # left + below
        end
        for history in reverse(histories)
            debug(history)
        end
        s += histories[begin][end]
        # break
    end

    close(f)

    s
end
result = work("09/sample.txt")
DEBUG=false
result = work("09/input.txt")
println("Result: ", result)
