using Test

function work(filepath::String)
    f = open(filepath)
    lines = readlines(f)
    close(f)

    # Sum
    su = 0

    # Create symbol mask
    symbol_lines = []
    for l in lines
        symbols = findall(r"[^\.\d]", l)
        v = zeros(Bool,1,length(l))
        for range in symbols
            v[range] .= 1
        end
        push!(symbol_lines, v)
    end

    symbol_matrix = vcat(symbol_lines...)
    r,c = size(symbol_matrix)
    display(symbol_matrix)

    # Create bound box for each number and slice symbol mask
    for (i,l) in enumerate(lines)
        numbers = findall(r"(\d+)", l)
        # println(l, " -> ", numbers)
        for range in numbers
            num = parse(Int,l[range])
            x_range = max(1, first(range)-1):min(c, last(range)+1)
            y_range = max(1, i-1):min(r, i+1)
            slice = symbol_matrix[y_range, x_range]
            hit = reduce(|, slice)
            # println(num, " ", x_range," ", y_range, " ", slice, " ", hit)
            if hit
                su += num
            end
        end
    end

    su
end
result = work("03/sample.txt")
result = work("03/input.txt")
println("Result: ", result)
