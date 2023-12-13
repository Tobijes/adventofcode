using Test
using LinearAlgebra
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


card_order = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]
card_strengths = Dict(a => i for (i,a) in enumerate(reverse(card_order)))
debug(card_strengths)

hand_maps = Dict(
    [5, 0, 0, 0, 0] => "FIVEKIND",
    [4, 1, 0, 0, 0] => "FOURKIND",
    [3, 2, 0, 0, 0] => "FULLHOUSE",
    [3, 1, 1, 0, 0] => "THREEKIND",
    [2, 2, 1, 0, 0] => "TWOPAIR",
    [2, 1, 1, 1, 0] => "ONEPAIR",
    [1, 1, 1, 1, 1] => "HIGHCARD"
)
hand_maps_reverse = Dict(value => key for (key, value) in hand_maps)
hand_order = ["FIVEKIND", "FOURKIND", "FULLHOUSE", "THREEKIND", "TWOPAIR", "ONEPAIR", "HIGHCARD"]
hand_strengths = Dict(a => i for (i,a) in enumerate(reverse(hand_order)))
debug(hand_strengths)


function hist(hand)
    histogram = Dict(card => 0 for card in card_order)
    hand_wo_jokers = replace(hand, "J" => "")
    for card in hand_wo_jokers
        histogram[string(card)] += 1
    end
    return sort(collect(values(histogram)), rev=true)
end

function best(histogram, len)
    jokers = len - sum(histogram) 
    debug(histogram)
    for name in hand_order
        hand = hand_maps_reverse[name]
        diff = norm(hand - histogram, 1)
        debug((histogram, hand, jokers,  diff))
        if diff <= jokers
            return hand
        end

    end
end

function lessthan(x,y) 
    (x_hand, x_bid, x_name, x_strength) = x
    (y_hand, y_bid, y_name, y_strength) = y

    if x_strength == y_strength
        x_numbers = map(c->card_strengths[c], split(x_hand, ""))
        y_numbers = map(c->card_strengths[c], split(y_hand, ""))
        # debug(x_hand, " ", x_numbers)
        # debug(y_hand, " ", y_numbers)
        for i in 1:length(x_numbers)
            if x_numbers[i] == y_numbers[i]
                continue
            end
            return x_numbers[i] < y_numbers[i]
        end
        return true
    else 
        return x_strength < y_strength
    end
end

function work(filepath::String)
    f = open(filepath)
    inputs = map(x-> cleansplit(x, " "),readlines(f))
    close(f)
    debug(inputs)

    hands = []

    for (hand, bid) in inputs
        histogram = hist(hand)[1:5]
        hand_name = haskey(hand_maps, histogram) ? hand_maps[histogram] : hand_maps[best(histogram, 5)]
        hand_strength = hand_strengths[hand_name]
        push!(hands, (hand, parse(Int, bid), hand_name, hand_strength))
    end

    debug(hands)

    sorted = sort(hands, by=x->x, lt=(x,y)->lessthan(x,y))
    debug(sorted)

    s = sum([bid * idx for (idx, (hand, bid, name, strength)) in enumerate(sorted)])
    s
end
result = work("07/sample.txt")
DEBUG = false
result = work("07/input.txt")
println("Result: ", result)
# @test result == 6440
