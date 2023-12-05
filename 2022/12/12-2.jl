using Test

@enum Direction left right up down

debug = false
p(s) = begin
    if debug
        println(s)
    end
end

STARTVAL = Int('a')
ENDVAL = Int('z') + 1

function available(coord, cur, M)
    if coord[1] == 0 || coord[2] == 0
        p(("Coord too small", coord))
        return false
    end

    (R,C) = size(M)
    if coord[1] > R || coord[2] > C
        p(("Coord too big", coord))
        return false
    end

    newOne = M[coord[1], coord[2]]
    if newOne == 1000
        return true
    end

    # if newOne < cur
    #     p(("Value is smaller", coord))
    #     return false
    # end

    if newOne > cur + 1 && cur != 0
        p(("Value is too big", coord))

        return false
    end

    true
end

function bfs(start, stop, M)
    q = [start]

    V = zero(M)
    V[start[1], start[2]] = 1

    parents = Dict()

    while !isempty(q)

        pos = popfirst!(q)
        if pos == stop
            println("Found END")
            # display(V)
            return parents
        end

        curVal = M[pos[1], pos[2]]

        up = pos + [-1, 0]
        left = pos + [0, -1]
        right = pos + [0, 1]
        down = pos + [1, 0]
        p((up, left, right, down))

        for e in [up, left, right, down]
            if available(e, curVal, M) && V[e[1], e[2]] == 0
                p(("Pushing", e))
                push!(q, e)
                V[e[1], e[2]] = 1
                parents[(e[1], e[2])] = (pos[1], pos[2])
            end
        end
    end
    println("We got a problem")
end

function findpath(parents, start, stop)
    # println(parents)
    path = []
    cur = stop
    while true
        push!(path, (cur[1], cur[2]))
        if cur == start
            break
        end
        cur = parents[(cur[1], cur[2])]
    end

    path
end

function work(filepath::String)
    f = open(filepath)

    rows = []
    for l in eachline(f)
        nums = map(collect(l)) do c
            if c == 'S'
                return 0
            elseif c == 'E'
                return ENDVAL
            end
            Int(c)
        end
        push!(rows,nums)
    end
    close(f)
    println(rows)

    M = transpose(hcat(rows...))
    display(M)

    startings = map(Tuple, findall(x->x==STARTVAL, M))
    (rE, cE) = Tuple(findall(x->x==ENDVAL, M)[1])

    lengths = []
    for (rS, cS) in startings
        parents = bfs([rS, cS], [rE, cE], M)
        if parents === nothing
            continue
        end
        path = findpath(parents, (rS, cS), (rE, cE))
        len = length(path) - 1
        println((rS, cS, rE, cE, len))
        push!(lengths, len)
    end

    min(lengths...)
end

# result = work("12/sample.txt")
result = work("12/input.txt")
println("Result: ", result)
@test result == 29
