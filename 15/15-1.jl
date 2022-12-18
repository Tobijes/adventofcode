using Test

Y = 10

dist(a,b) = sum(abs.(a - b))

function points(sx,sy,dx,dy)
    valid = Set()
    d = dx+dy

    # Filter sensors
    fromY = abs(Y - sy)
    if sy > Y && sy - d > Y
        return valid
    end

    if sy < Y && sy + d < Y
        return valid
    end

    off = max(dx,dy)
    for x in sx-off:sx+off # need to reduce this
        if dist([sx, sy], [x,Y]) > d
            # println(d)
            continue
        end
        push!(valid, [x,Y])
    end
    valid
end

function work(filepath::String)
    f = open(filepath)

    sensor2beacon = Dict()
    for l in eachline(f)
        matches = map(x->parse(Int64, x), [m[1] for m in eachmatch(r"(-?\d+)", l)])
        (sx,sy,bx,by) = matches
        sensor2beacon[[sx,sy]] = [bx, by]
        # println(matches)
    end

    close(f)

    sensors = collect(keys(sensor2beacon))

    cannot = Set()
    for sensor in sensors
        # println(sensor)
        nearest = sensor2beacon[sensor]
        # println((sensor, nearest))
        distance = dist(sensor, nearest)
        (dx,dy) = abs.(sensor - nearest)
        # distance = abs(sensor[1] - nearest[1]) + abs(sensor[2] - nearest[2])
        println((sensor, nearest, dx,dy))
        (sx,sy) = sensor
        ps = points(sx,sy,dx,dy)
        if length(ps) > 0
            push!(cannot, ps...)
        end

    end

    beacons = Set(values(sensor2beacon))
    setdiff!(cannot, beacons)

    # println((sensors, beacons))
    length(cannot)
end
result = work("15/sample.txt")
result = work("15/input.txt")
println("Result: ", result)
@test result == 26
