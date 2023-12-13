using Test

DEBUG = true

function debug(args...)
    if DEBUG
        println(args...)
    end
end

function cleansplit(s::AbstractString, sep::String)
    splitted = split(s, sep, keepempty=false)
    map(x->strip(x), splitted)
end

function iswin(time, hold, record)
    (time - hold) * hold > record
end

function n_wins(maxtime, record)
    s = sum([iswin(maxtime, hold, record) for hold in 1:maxtime])
    debug("n_wins | maxtime: ", maxtime, " record: ", record, " sum: ", s)
    s
end

function work(filepath::String)
    # Read file
    f = open(filepath)
    lines = readlines(f)
    close(f)

    # Parse input
    times = parse.(Int, cleansplit(lines[1], " ")[2:end])
    distances = parse.(Int, cleansplit(lines[2], " ")[2:end])
    debug(times)
    debug(distances)

    result = prod([n_wins(times[i], distances[i]) for i in 1:length(times)])

    result
end
DEBUG = true
result = work("06/sample.txt")
DEBUG = false
result = work("06/input.txt")
println("Result: ", result)
