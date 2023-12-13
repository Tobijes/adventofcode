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

function array_lcm(arr)
    result = arr[1]
    for i in 2:length(arr)
        result = lcm(result, arr[i])
    end
    return result
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
    current_last = collect(map(x->x[end], current))
    simous = length(current)
    debug(current)
    
    looplength = []
    
    for i in 1:simous  
        steps = 0
        run = true
        while run
            debug(("Steps", steps))
            for dir in instr
                steps += 1
                idx = dir == "L" ? 1 : 2
                current[i] = themap[current[i]][idx]
                current_last[i] = current[i][end]
                debug((current, current_last))
                
            end
            if current_last[i] == 'Z'
                run = false
            end
        end
        push!(looplength, steps)
    end

    println(("Loop length", looplength))
    reduce(lcm, looplength) 
end
result = work("08/sample2.txt")
DEBUG=false
result = work("08/input.txt")
println("Result: ", result)
