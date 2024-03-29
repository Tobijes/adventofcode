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
    instr = split(readline(f), "")
    readline(f)
    
    themap = Dict()
    regex = r"(\w+) = \((\w+)\, (\w+)\)"
    for l in eachline(f)
        m = match(regex, l)
        (start, left, right) = m.captures
        themap[start] = (left, right)
    end

    close(f)

    debug(instr)
    debug(themap)

    current = "AAA"
    steps = 0
    while current != "ZZZ"
        for dir in instr
            steps += 1
            if dir == "L"
                current = themap[current][1]
            else
                current = themap[current][2]
            end
        end
    end

    steps
end
result = work("08/sample.txt")
DEBUG=false
result = work("08/input.txt")
println("Result: ", result)
