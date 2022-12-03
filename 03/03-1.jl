function cnv2priority(symbol::Char)

    sep = Int('a')
    s = Int(symbol)
    if s >= sep
        return s - 96 # Map from ASCII
    else
        return s - 64 + 26 # Map from ASCII, flip abc.. and ABC...
    end
end

function evaluate(rucksack::String)

    splitIdx = length(rucksack) ÷ 2
    c1 = Set(rucksack[1:splitIdx])
    c2 = Set(rucksack[splitIdx+1:end])

    # println((c1,c2))

    repeats = intersect(c1,c2)

    symbol = first(repeats)
    cnv = cnv2priority(symbol) 
    # println((symbol, cnv))
    
    cnv
end

function work(filepath::String)
    f = open(filepath)

    mySum = 0
    for l in eachline(f)
        priority = evaluate(l)
        mySum += priority
    end

    close(f)

    mySum
end

work("03/input.txt")
