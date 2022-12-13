using Test

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
            # println(buf)
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
    println((first,second))
    if first isa Int64 && second isa Int64
        println(("Both ints", first, second))
        if first == second
            return nothing
        elseif first > second
            return false
        end
        return true
    end

    if first isa Vector{} && second isa Vector{}
        println(("Both lists", first, second))
        len1 = length(first)
        len2 = length(second)

        idx = 0

        for i in 1:min(len1, len2)
            println(i)

            r = compare(first[i], second[i])
            if r !== nothing && r == true
                return true
            end
            idx = i
        end

        if idx < len2
            # Left side ran out
            return true
        end
        return false
    end

    if first isa Int64
        println(("First is int", first, second))
        return compare([first], second)
    end
    if second isa Int64
        println(("Second is int", first, second))
        return compare(first, [second])
    end

    return true
end

compare([[1],[2,3,4]], [[1],4])

# function work(filepath::String)
#     f = open(filepath)

#     pairs = []
#     currentPair = []
#     for l in eachline(f)

#         if length(currentPair) == 2
#             push!(pairs, currentPair)
#             currentPair = []
#         end

#         push!(currentPair, treelike(l))
#     end

#     close(f)


#     println(pairs)

#     0
# end
# # treelike("[1,[2,[3,[4,[5,6,7]]]],8,9]")
# result = work("13/sample.txt")
# #result = work("13/input.txt")
# println("Result: ", result)
# @test result == 13
