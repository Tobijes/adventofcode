using Test

function work(filepath::String)
    f = open(filepath)
    lines = readlines(f)
    close(f)

    # Create symbol mask
    symbol_lines = []
    gear_parts = Dict()
    for (i,l) in enumerate(lines)
        symbols = [first(r) for r in findall("*", l)]
        v = zeros(Bool,1,length(l))
        for loc in symbols
            v[loc] = 1
            gear_parts[(i, loc)] = []
        end
        push!(symbol_lines, v)
    end

    symbol_matrix = vcat(symbol_lines...)
    r,c = size(symbol_matrix)
    display(symbol_matrix)
    println(gear_parts)


    # Create bound box for each number and slice symbol mask
    for (i,l) in enumerate(lines)
        numbers = findall(r"(\d+)", l)
        # println(l, " -> ", numbers)
        for range in numbers
            num = parse(Int,l[range])
            x_range = max(1, first(range)-1):min(c, last(range)+1)
            y_range = max(1, i-1):min(r, i+1)
            slice = symbol_matrix[y_range, x_range]
            # println("Slice range: ", [y_range, x_range])
            gears = findall(x -> x == true, slice )
            # println(gears)
            for gear in gears
                push!(gear_parts[(gear[1]+first(y_range)-1, gear[2]+first(x_range)-1)], num)
            end
        end
    end
    # println(gear_parts)


    # Sum
    su = 0

    gear_parts = filter(p -> length(p[2]) == 2, gear_parts)
    for (k,v) in gear_parts
        su += prod(v)
    end
    su
end
result = work("03/sample.txt")
result = work("03/input.txt")
println("Result: ", result)
