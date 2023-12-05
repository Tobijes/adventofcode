using Test

function cleansplit(s::AbstractString, sep::String)
    splitted = split(s, sep, keepempty=false)
    map(x->strip(x), splitted)
end

function work(filepath::String)
    f = open(filepath)

    su = 0

    for l in eachline(f)

        card, numbers = cleansplit(l, ":")
        # println(numbers)
        yours, winning  = cleansplit(numbers, "|")

        winning = cleansplit(winning, " ")
        winning = map(x->parse(Int, x), winning)
        winning = Set(winning)

        yours = cleansplit(yours, " ")
        yours = map(x->parse(Int, x), yours)
        yours = Set(yours)

        inter = intersect(winning, yours)
        # println(winning, yours, inter)

        n = length(inter)
        if n < 1
            continue
        end

        points = 2^(n-1)
        # println("Points: ", points)
        su += points
    end

    close(f)

    su
end
result = work("04/sample.txt")
result = work("04/input.txt")
println("Result: ", result)
