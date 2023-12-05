using DataStructures

function cleansplit(s::AbstractString, sep::String)
    splitted = split(s, sep, keepempty=false)
    map(x->strip(x), splitted)
end

function work(filepath::String)
    queue = Queue{Int}()
    counters = Dict()
    cardwins = Dict()
    f = open(filepath)

    for l in eachline(f)

        card, numbers = cleansplit(l, ":")

        cardword, cardnum = cleansplit(card, " ")
        cardnum = parse(Int, cardnum)
        counters[cardnum] = 0
        # println(cardnum)
        # println(numbers)
        yours, winning  = cleansplit(numbers, "|")

        winning = cleansplit(winning, " ")
        winning = map(x->parse(Int, x), winning)
        winning = Set(winning)

        yours = cleansplit(yours, " ")
        yours = map(x->parse(Int, x), yours)
        yours = Set(yours)

        inter = intersect(winning, yours)
        cardwins[cardnum] = length(inter)

        enqueue!(queue, cardnum)
    end

    close(f)

    println(cardwins)
    println(counters)

    while !isempty(queue)
        cardnum = dequeue!(queue)
        counters[cardnum] += 1
        wins = cardwins[cardnum]
        for card in (cardnum+1):(cardnum+wins)
            enqueue!(queue, card)
        end
    end
    println(counters)

    sum(values(counters))
end
result = work("04/sample.txt")
result = work("04/input.txt")
println("Result: ", result)
