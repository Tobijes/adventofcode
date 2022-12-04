function contains(p1::Tuple{Int64, Int64}, p2::Tuple{Int64, Int64})
    p2[1] >= p1[1] && p2[2] <= p1[2]
end

function evaluate(line::String)

    c1, c2 = split(line, ",")

    ps(rng)=map(split(rng, "-")) do s parse(Int64, s) end
        
    # println((c1,c2))
    c1s, c1e = ps(c1)
    c2s, c2e = ps(c2)
    # println((c1s, c1e, c2s, c2e))
    
    if contains((c1s,c1e), (c2s, c2e)) || contains((c2s, c2e), (c1s,c1e))
        return 1
    end
        
    0
end

function work(filepath::String)
    f = open(filepath)

    mySum = 0
    for l in eachline(f)
        result = evaluate(l)
        mySum += result
    end

    close(f)

    mySum
end

work("04/input.txt")
