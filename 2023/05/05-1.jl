using Test

struct MapRange
    sourceStart::Int
    destinationStart::Int
    size::Int
end

function cleansplit(s::AbstractString, sep::String)
    splitted = split(s, sep, keepempty=false)
    map(x->strip(x), splitted)
end

function work(filepath::String)
    f = open(filepath)

    l = readline(f)
    seeds = parse.(Int, cleansplit(replace(l, "seeds: " => ""), " "))
    # println(seeds)

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
        
        numbers = parse.(Int, cleansplit(l, " "))
        mapRange = MapRange(numbers[2], numbers[1], numbers[3])
        push!(maps[end], mapRange)
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
    for seed in seeds
        num = seed
        print("Seed: ", num)
        for map in maps
            # println(map)
            for maprange in map
                # println(maprange)
                if maprange.sourceStart <= num < maprange.sourceStart+maprange.size
                    # println("THis")
                    num = maprange.destinationStart + (num-maprange.sourceStart)
                    break
                end
            end
            print(" ", num)
        end
        println()
        push!(locations, num)
    end
    println(locations)
    minimum(locations)
end
result = work("05/sample.txt")
result = work("05/input.txt")
println("Result: ", result)
# @test result == 35
