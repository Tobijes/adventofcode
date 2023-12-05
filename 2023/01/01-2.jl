using Test

num_dict = Dict("one" => 1, "two" => 2, "three" => 3, "four" => 4, "five" => 5, "six" => 6, "seven" => 7, "eight" => 8, "nine" => 9)

function translate(str::String)

    if haskey(num_dict, str)
        return string(num_dict[str])
    end
    str
end

function parse_line(str::String)

    matches = [string(m.match) for m in eachmatch(r"(one|two|three|four|five|six|seven|eight|nine|\d)", str, overlap=true)]
    fst = translate(first(matches))
    lst = translate(last(matches))
    combined = fst * lst
    parse(Int, combined)
end

function work(filepath::String)
    f = open(filepath)

    su = 0
    for l in eachline(f)
        ls = parse_line(l)
        println(l, " -> ", ls)
        su += ls
    end

    close(f)

    su
end
result = work("01/sample.txt")
result = work("01/input.txt")
println("Result: ", result)
