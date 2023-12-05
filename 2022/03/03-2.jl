function cnv2priority(symbol::Char)

    sep = Int('a')
    s = Int(symbol)
    if s >= sep
        return s - 96 # Map from ASCII
    else
        return s - 64 + 26 # Map from ASCII, flip abc.. and ABC...
    end
end

function evaluate(group::Array{String, 1})

    c1 = Set(group[1])
    c2 = Set(group[2])
    c3 = Set(group[3])

    badge = first(intersect(intersect(c1, c2), c3))
    cnv = cnv2priority(badge)
    # println((group, badge, cnv))
    
    cnv
end

function work(filepath::String)
    f = open(filepath)

    mySum = 0

    group::Array{String, 1} = []
    for l in eachline(f)
        push!(group, l)
        if length(group) == 3
            typeof(group)
            priority = evaluate(group)
            mySum += priority
            group = []
        end
    end

    close(f)

    mySum
end

work("03/input.txt")
