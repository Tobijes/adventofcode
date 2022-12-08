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
    display(M)

    V = zero(M)
    display(V)
    
    V[1:end,1] .= 1
    V[1:end,end] .= 1
    V[1,1:end] .= 1
    V[end,1:end] .= 1
    display(V)

    rs,cs = size(V)

    smaller(num, lst)= begin
        all(num .> lst)
    end

    for r in 2:cs-1
        for c in 2:rs-1
            v = M[r,c]
            up = M[1:r-1, c]
            down = M[r+1:end, c]
            left = M[r, 1:c-1]
            right = M[r, c+1:end]
            # println((up, down, left, right))

            if smaller(v, up) || smaller(v, down) || smaller(v, left) || smaller(v, right)
                # println((r,c, "true"))
                V[r,c] = 1
            end
            
        end
        
    end

    sum(V)
end

result = work("08/sample.txt")
#result = work("08/input.txt")
# println("Result: ", result)
@test result == 21
