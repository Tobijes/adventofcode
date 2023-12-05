using Test

MAX = Dict(
    "red" => 12,
    "green" => 13,
    "blue" => 14
)
function work(filepath::String)
    f = open(filepath)

    id_sum = 0

    for l in eachline(f)
        println(l)
        parts = split(l, ":")
        # Find ID
        id_part = parts[1]
        id = parse(Int, id_part[6:end])

        # Find sets
        sets = split(parts[2], ";")
        impossible = false
        for set in sets
            if impossible
                break
            end
            println(set)

            groups = split(set, ",")

            for group in groups
                num, name = split(strip(group), " ")
                num_int = parse(Int, num)

                if num_int > MAX[name]
                    println("Impossible!")
                    impossible = true
                    break
                end
            end
        end

        if !impossible
            println("Adding ID", id)
            id_sum += id
        end
    end

    close(f)

    id_sum
end
result = work("02/sample.txt")
result = work("02/input.txt")
println("Result: ", result)
