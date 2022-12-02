
function work(filepath::String)

    f = open(filepath)

    mxVal = 0
    curVal = 0

    for l in eachline(f)
        println(l)
        if l == ""
            mxVal = max(mxVal, curVal)
            curVal = 0
        else
            curVal += parse(Int64, l)
        end
    end


    close(f)

    mxVal
end

work("01/input.txt")
