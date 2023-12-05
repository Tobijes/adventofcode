using Test

function work(filepath::String)
    f = open(filepath)

    su = 0

    for l in eachline(f)
        println(l)
        parts = split(l, ":")

        # Find sets
        sets = split(parts[2], ";")


        mins = Dict(
            "red" => 0,
            "green" => 0,
            "blue" => 0
        )
        for set in sets

            println(set)

            groups = split(set, ",")

            for group in groups
                num, name = split(strip(group), " ")
                num_int = parse(Int, num)

                mins[name] = max(mins[name], num_int)
            end
        end

        println(mins)
        su += prod(values(mins))
    end

    close(f)

    su
end
result = work("02/sample.txt")
result = work("02/input.txt")
println("Result: ", result)
