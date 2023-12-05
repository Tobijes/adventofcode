tOpponent = Dict('A' => 1, 'B' => 2, 'C' => 3)
tYou = Dict('X' => 1, 'Y' => 2, 'Z' => 3)
wpnPnt = Dict('X' => 1, 'Y' => 2, 'Z' => 3)

# Fight result
#       You
#      R P S
#      1 2 3
# R 1: 3 6 0
# P 2: 0 3 6
# S 3: 6 0 3

rYou = [
    3 6 0;
    0 3 6;
    6 0 3
]

# Returns the score for you
function evaluate(opponent::Char, you::Char)

    idxO = tOpponent[opponent]
    idxY = tYou[you]

    wpnPnt[you] + rYou[idxO, idxY]

end

function work(filepath::String)
    f = open(filepath)

    mySum = 0
    for l in eachline(f)
        pnt = evaluate(l[1], l[3])
        mySum += pnt
        #println((l, pnt))

    end

    close(f)

    mySum
end

work("02/input.txt")
