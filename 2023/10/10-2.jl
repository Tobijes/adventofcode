using Test
using DataStructures

DEBUG = true

function debug(args...)
    if DEBUG
        println(args...)
    end
end

function mdebug(arg)
    if DEBUG
        display(arg)
    end
end

function cleansplit(s::AbstractString, sep::String)
    splitted = split(s, sep, keepempty=false)
    map(x->strip(x), splitted)
end

function get_clamped_possible_positions(position, size)
    diretions = [
        (position[1]-1, position[2] ),
        (position[1]+1, position[2] ),
        (position[1], position[2]-1 ),
        (position[1], position[2]+1 ),
    ]

    return filter(x -> 0 < x[1] <= size[1] &&  0 < x[2] <=size[2], diretions)
end

# Contains the usable direction of tokens. Addition requried to CUR to join
joins = Dict(
    "S" => [(1,0),(0,1),(-1,0),(0,-1)],
    "|" => [(1,0), (-1,0)],
    "-" => [(0,-1), (0,1)],
    "L" => [(1,0), (0,-1)],
    "J" => [(1,0), (0,1)],
    "7" => [(-1,0), (0,1)],
    "F" => [(-1,0), (0,-1)],
    "." => [],
)

function work(filepath::String)
    f = open(filepath)
    lines = readlines(f)
    close(f)
    themap = collect(map(x->string.(split(x,"")), lines))
    themap = mapreduce(permutedims, vcat, themap)
    debug(themap)
    mdebug(themap)
    start_pos = Tuple(findfirst(x->x=="S",themap))
    sz = size(themap)
    debug(sz)
    debug(start_pos)

    marks = ones(Int, sz) * -1
    mdebug(marks)
    queue = Queue{Tuple{Int, Int}}()
    marks[start_pos...] = 0
    enqueue!(queue, start_pos)
    
    while !isempty(queue)
        curpos = dequeue!(queue)
        positions = get_clamped_possible_positions(curpos, sz)
        # debug(positions)

        for pos in positions
            join = themap[pos[1], pos[2]]
            allowed_dirs = joins[join]
            dir = pos .- curpos 
            # debug((join, allowed_dirs, dir))
            
            if dir ∉ allowed_dirs
                continue
            end

            if marks[pos...] >= 0
                continue
            end
            
            marks[pos...] = marks[curpos...] + 1
            debug(("Move to", pos))
            enqueue!(queue, pos)
            
        end
    end

    mdebug(marks)

    
    0
end
result = work("10/sample2.txt")
DEBUG=false
# result = work("10/input.txt")
println("Result: ", result)
