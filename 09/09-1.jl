using Test

function moveH(current, dir)
    if dir == "U"
        return current + [0,1]
    elseif dir == "R"
        return current + [1,0]
    elseif dir == "D"
        return current + [0,-1]
    elseif dir == "L"
        return current + [-1,0]
    end
end

function moveT(currentT, H)
    rowsaway = abs(H[2] - currentT[2])
    colsaway = abs(H[1] - currentT[1])
    # If touching or overlapping
    if rowsaway + colsaway <= 1 || (rowsaway == 1 && colsaway == 1)
        return currentT
    end
    
    dif = [H[1] - currentT[1], H[2] - currentT[2]]
    realMove = (dif / 2)
    move = round.(Int, realMove, RoundNearestTiesAway)
    # println((currentT, dif, move))
    currentT + move
end

function work(filepath::String)
    f = open(filepath)
    H = [0,0]
    T = [0,0]
    positions = Set([[0,0]])

    for l in eachline(f)
        (dir, num) = split(l, " ")
        # println((dir, num))
        for i in 1:parse(Int64, num)
            H = moveH(H, dir)
            # println(("H", H))
            T = moveT(T, H)
            # println(("T", T))
            push!(positions, T)
        end
    end

    close(f)

    length(positions)
end

# result = work("09/sample.txt")
result = work("09/input.txt")
println("Result: ", result)
# @test result == 13
