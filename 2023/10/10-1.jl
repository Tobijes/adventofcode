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

function get_directions(themap)
end
function work(filepath::String)
    f = open(filepath)
    
    themap = collect(map(x->split(x,""), readlines(f)))
    close(f)
    debug(themap)
    display(themap)
    start_pos = findfirst(x->x=="S",themap)
    debug(start_pos)

    0
end
result = work("10/sample.txt")
DEBUG=false
#result = work("10/input.txt")
println("Result: ", result)
