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


    current = collect(filter(x-> x[end] == 'A', keys(themap) ))
    simous = length(current)
    debug(current)
    steps = 0
    while any(map(x->x[end], current) .!= 'Z')
        for dir in instr
            steps += 1
            if dir == "L"
                for i in 1:simous
                    current[i] = themap[current[i]][1]
                end
            else
                for i in 1:simous
                    current[i] = themap[current[i]][2]
                end
            end
            debug(current)
        end
    end

    steps
end
result = work("08/sample2.txt")
DEBUG=false
result = work("08/input.txt")
println("Result: ", result)
