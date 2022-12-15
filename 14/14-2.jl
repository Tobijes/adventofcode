using Test

function disp(rocks, sand)
    xs = map(x->x[1], collect(union(rocks, sand)))
    ys = map(x->x[2], collect(union(rocks, sand)))
    xmin, xmax = min(xs..., 500), max(xs..., 500)
    ymin, ymax = min(ys...,0), max(ys...,0)
    println((xmin, xmax, ymin, ymax))

    for y in ymin:ymax+2
        for x in xmin:xmax
            point = [x,y]
            if point == [500, 0]
                print("+") 
            elseif point in rocks
                print("#")
            elseif point in sand
                print("o")
            elseif y == ymax+2
                print("#")
            else
                print(".")
            end
        end
        println()
    end
end

function work(filepath::String)
    f = open(filepath)

    rocks = Set()
    for l in eachline(f)
        knots = map(split(l, " -> ")) do k
            (xs, ys) = split(k, ",")
            [parse(Int64, xs),parse(Int64, ys)]
        end
        
        for i in 1:(length(knots)-1)
            from = knots[i]
            to = knots[i+1]
            xmin = min(from[1], to[1])
            xmax = max(from[1], to[1])
            ymin = min(from[2], to[2])
            ymax = max(from[2], to[2])

            # println((from, to))
            for x in xmin:xmax
                for y in ymin:ymax
                    # println((x,y))
                    push!(rocks, [x,y])
                end
            end
        end
    end
    close(f)
    # println(rocks)

    sand = Set()
    disp(rocks, sand)
    # return
    # Simulate

    ys = map(x->x[2], collect(rocks))
    ymin, ymax = min(ys...,0), max(ys...,0)

    down = [0,1]
    downleft = [-1,1]
    downright = [1,1]

    # Every sand
    while true
        cur = [500, 0]
        block = union(rocks, sand)

        # Run single sand
        for i in 1:ymax+3

            if !(cur + down in block) && !((cur + down)[2] == ymax+2)
                cur += down
                continue
            end

            if !(cur + downleft in block) && !((cur + downleft)[2] == ymax+2)
                cur += downleft
                continue
            end

            if !(cur + downright in block) && !((cur + downright)[2] == ymax+2)
                cur += downright
                continue
            end
            
            push!(sand, cur)
            break
        end
        
        if cur == [500,0]
            println("Reached top")
            break
        end
        
    end

    disp(rocks, sand)

    length(sand)
end
# result = work("14/sample.txt")
result = work("14/input.txt")
println("Result: ", result)
@test result == 93
