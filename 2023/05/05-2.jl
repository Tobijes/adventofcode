using Test
using DataStructures

struct MapRange
    sourceStart::Int
    sourceStop::Int
    destinationStart::Int
    destinationStop::Int
end

struct Range
    start::Int
    stop::Int
    level::Int
end

function cleansplit(s::AbstractString, sep::String)
    splitted = split(s, sep, keepempty=false)
    map(x->strip(x), splitted)
end

function validrange(start, stop)
    return stop - start >= 0
end

function work(filepath::String)
    f = open(filepath)

    l = readline(f)
    seeds = parse.(Int, cleansplit(replace(l, "seeds: " => ""), " "))
    ranges = [Range(seeds[i], seeds[i]+seeds[i+1]-1, 1) for i in 1:2:length(seeds) ]

    names = []
    maps = []

    for l in eachline(f)
        if occursin("map", l)
            push!(maps, [])
            push!(names, first(cleansplit(l, " ")))
            continue
        end

        if length(l) < 2
            continue
        end
        
        destinationStart, sourceStart, size = parse.(Int, cleansplit(l, " "))
        mapRange = MapRange(sourceStart, sourceStart + size-1, destinationStart, destinationStart + size-1)
        push!(maps[end], mapRange)
    end

    for map in maps
        sort!(map,by=x->x.sourceStart)
    end

    close(f)

    for (name, map) in zip(names, maps)
        println(name, ":")
        for range in map
            println(range)
        end
        println()
    end
    
    locations = []
    queue = Queue{Range}()
    for range in ranges
        enqueue!(queue, range)
    end

    while !isempty(queue)

        range = dequeue!(queue)
        println("Dequeued range: ", range)
        if range.level > length(maps)
            push!(locations, range.start)
            continue
        end

        start = range.start
        stop = range.stop
        
        # For each maprange in the current map
        for maprange in maps[range.level]

            # Part inside 
            insideStart = max(range.start, maprange.sourceStart)
            insideStop = min(range.stop, maprange.sourceStop)
            
            if validrange(insideStart, insideStop)
                newStart = maprange.destinationStart + (insideStart - maprange.sourceStart)
                newStop = maprange.destinationStart + (insideStop - maprange.sourceStart)
                newRange = Range(newStart, newStop, range.level + 1)
                println("Enquing inside:, ", newRange)
                enqueue!(queue, newRange)
            end

            # Part before
            beforeStart = range.start
            beforeStop = insideStart - 1

            if validrange(beforeStart, beforeStop)
                newRange = Range(beforeStart, beforeStop, range.level + 1)
                println("Enquing before:, ", newRange)
                enqueue!(queue, newRange)
            end

            # Part after
            start = max(range.start, maprange.sourceStop) + 1
            stop = range.stop

            println("After Start Stop ", start, " ", stop)
            if !validrange(start, stop)
                break
            end
        end

        if validrange(start, stop)
            newRange = Range(start, stop, range.level + 1)
            println("Enquing after:, ", newRange)
            enqueue!(queue, newRange)
        end
    end
    
    println(locations)
    minimum(locations)
end
result = work("05/sample.txt")
# result = work("05/input.txt")
println("Result: ", result)
# @test result == 35
