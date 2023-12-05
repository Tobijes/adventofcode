using Test

function parse_line(str::String)

    matches = [m for m in eachmatch(r"\d", str)]

    combined = first(matches).match * last(matches).match
    parse(Int, combined)
end

function work(filepath::String)
    f = open(filepath)

    su = 0
    for l in eachline(f)
        su += parse_line(l)
    end

    close(f)

    su
end
# result = work("01/sample.txt")
result = work("01/input.txt")
println("Result: ", result)
