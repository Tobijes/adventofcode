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
    all = [[0,0] for _ in 1:10]

    positions = Set([[0,0]])

    for l in eachline(f)
        (dir, num) = split(l, " ")
        # println((dir, num))
        for _ in 1:parse(Int64, num)
            all[1] = moveH(all[1], dir)
            for j in 2:length(all)
                all[j] = moveT(all[j], all[j-1])
            end
            # println(all)

            push!(positions, all[end])
        end
    end

    close(f)

    length(positions)
end

# result = work("09/sample2.txt")
result = work("09/input.txt")
println("Result: ", result)
@test result == 36
