using Test

debug = false
p(s) = begin
    if debug
        println(s)
    end
end

struct Node
    parent::Any
    children::Array{Any, 1}
end

function treelike(s)
    s=s[2:end]
    root = Node(nothing,[])
    cur = root
    buf = ""


    for (i, c) in enumerate(s)
        if c == '['
            n = Node(cur, [])
            push!(cur.children, n)
            cur = n
        elseif c == ']'
            if buf!=""
                push!(cur.children, buf)
                buf = ""
            end
            cur = cur.parent
        elseif c == ','
            if buf!=""
                push!(cur.children, buf)
                buf = ""
            end
        else
            buf *= c
            # p(buf)
        end
    end
    if buf != ""
        push!(root.children, buf)
        buf = ""
    end

    tolists(root)
end

function tolists(node)
    if node isa String
        return parse(Int64, node)
    end
    map(x->tolists(x), node.children)
end

function compare(first, second)
    p(("Compare", first,second))
    if first isa Int64 && second isa Int64
        p(("Both ints", first, second))
        if first == second
            return nothing
        elseif first > second
            return false
        end
        return true
    end

    if first isa Vector{} && second isa Vector{}
        p(("Both lists", first, second))
        len1 = length(first)
        len2 = length(second)

        idx = 0

        for i in 1:max(len1, len2)
            p(i)

            if i > len1
                p("left side ran out")
                return true
            end

            if i > len2
                p("right side ran out")
                return false
            end

            r = compare(first[i], second[i])
            if r === nothing
                idx = i
                continue
            end
            
            if r == true
                p(("First is smallest", first[i], second[i]))
                return true
            else p(("Seconds is smallest", first[i], second[i]))
                return false
            end
        end

        return nothing
    end

    if first isa Int64
        p(("First is int", first, second))
        return compare([first], second)
    end
    if second isa Int64
        p(("Second is int", first, second))
        return compare(first, [second])
    end

    return true
end


function work(filepath::String)
    f = open(filepath)

    signals = []
    for l in eachline(f)
        if l == ""
            continue
        end
        
        println(l)
        push!(signals, treelike(l))

    end

    push!(signals,[[2]])
    push!(signals,[[6]])

    close(f)
    p(signals)
    sortedSignals = sort(signals, lt=(f,s) -> compare(f,s))
    start = 0
    stop = 0
    for (i,s) in enumerate(sortedSignals)
        if s == [[2]]
            start = i
        end
        if s == [[6]]
            stop = i
        end
        # println(s)
    end
    # println((start, stop))
    start*stop
end
# result = compare([[1],[2,3,4]],[[1],4])
# result = compare([7,7,7,7],[7,7,7])
# treelike("[1,[2,[3,[4,[5,6,7]]]],8,9]")
result = 0
# result = work("13/sample.txt")
result = work("13/input.txt")
println("Result: ", result)
@test result == 140
