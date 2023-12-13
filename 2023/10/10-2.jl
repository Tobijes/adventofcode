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

function work(filepath::String)
    f = open(filepath)


    for l in eachline(f)

    end

    close(f)

    0
end
result = work("10/sample.txt")
DEBUG=false
#result = work("10/input.txt")
println("Result: ", result)
