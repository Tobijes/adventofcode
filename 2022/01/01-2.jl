# Easy peasy sort-based solution
function work(filepath::String)

    f = open(filepath)


    all = []


    curVal = 0

    for l in eachline(f)
        if l == ""
            push!(all, curVal)
            curVal = 0
        else
            curVal += parse(Int64, l)
        end
    end


    close(f)

    sort!(all) 

    sum(all[end-2:end])
end

work("01/input.txt")
