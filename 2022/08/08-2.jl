using Test

function evaluate(line::String)
        
    0
end

function work(filepath::String)
    f = open(filepath)

    rows = []
    for l in eachline(f)
        cols = split(l, "")
        colsInt = map(x->parse(Int64, x), cols)
        push!(rows, colsInt)
    end

    close(f)

    M = transpose(hcat(rows...))
    # display(M)

    V = zero(M)
    # display(V)

    rs,cs = size(V)

    score(num, lst)= begin
        s = 0
        for see in lst
            if num > see
                s += 1
            elseif num <= see
                s += 1
                break
            end
        end
        s
    end

    for r in 2:rs-1
        for c in 2:cs-1
            # println((r,c))
            v = M[r,c]
            up = reverse(M[1:r-1, c])
            down = M[r+1:end, c]
            left = reverse(M[r, 1:c-1])
            right = M[r, c+1:end]
            
            # println((up, down, left, right, v))
            # println((score(v, up), score(v, down),score(v, left),score(v, right)))
            V[r,c] = score(v, up) * score(v, down) * score(v, left) * score(v, right)
            # println((up, down, left, right, v, V[r,c]))
            
        end
        
    end
    # display(V)
    # show(stdout, "text/plain", V)
    # println()

    maximum(V)
end

# result = work("08/sample.txt")
result = work("08/input.txt")
# println("Result: ", result)
# @test result == 8
