using Test

function evaluate(line::String)
        
    0
end

function interpret(l::String)
    pattern = r"move (\d+) from (\d+) to (\d+)"
    matches = map(collect(match(pattern, l))) do k parse(Int64, k) end
    (amount, from, to) = matches
    (amount, from, to)
end

function create(size::Int64, lines)
    
    stacks = [[] for i in 1:size]

    pattern = r"(\s\s\s|\[.\])\s?"
    foreach(lines) do l
        # println(l)
        # println(eachmatch(pattern, l))
        for (i,m) in enumerate(eachmatch(pattern, l))
            mtch = m[1]
            # println(mtch)

            if occursin('[', mtch)
                push!(stacks[i], mtch[2])
            end
        end
    end

    println(stacks)
    map(stacks) do s length(s) > 0 ? reverse!(s) : s end
    println(stacks)
    stacks
end

function work(filepath::String)
    f = open(filepath)

    size = 0
    
    lines = []
    stacks = []

    
    for l in eachline(f)

        # Stage 1
        if size == 0
            if occursin("[", l)
                push!(lines, l)
            else 
                size = parse(Int64, last(split(l)))
                println(("Size", size))
                stacks = create(size, lines)
                
            end
            continue
        end
        
        # Stage 2
        if length(l) == 0
            continue
        end
        cmd = interpret(l)
        println(cmd)
        (amount, from, to) = cmd
        moves = reverse([pop!(stacks[from]) for _ in 1:amount])
        println(moves)
        append!(stacks[to], moves)
        
    end
    close(f)
    println(("Stacks", stacks))
    join(map(stacks) do s last(s) end)
end

result = work("05/input.txt")
#result = work("05/input.txt")
println("Result: ", result)
