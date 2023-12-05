using Test


struct File
    name::String
    size::Int64
end

mutable struct Directory
    name::String
    parent::Any
    children::Dict{String, Any}
    size::Int64
end

struct Root
    children::Dict{String, Any}
end

function visualize(dir::Directory, level::Int64)

    for (k, v) in dir.children

        if v isa File
            println("  "^level * "- " * v.name * " (" * string(v.size) * ")")
        elseif v isa Directory
            println("  "^level * "- " * v.name * "/ (" * string(v.size) * ")")
            visualize(v, level+1)
        end
    end


end

function dirSize(dir::Directory)
    mySum = 0
    for (k, v) in dir.children

        if v isa File
            mySum += v.size
        elseif v isa Directory
            mySum += v.size
        end
    end
    mySum
end

function setsizes(dir::Directory)

    for (k, v) in dir.children

        if v isa Directory
            setsizes(v)
        end
    end

    dir.size = dirSize(dir)

end

function listsizes(dir::Directory)::Array{Int64, 1}
    myLst::Array{Int64, 1} = []

    for (k, v) in dir.children
        if v isa Directory
            lst = listsizes(v)
            append!(myLst, lst)
        end
    end
    push!(myLst, dir.size)
    myLst
end

function work(filepath::String)
    f = open(filepath)

    # Build tree
    system = Root(Dict{String, Any}())
    system.children["/"] = Directory("/", system, Dict{String, Any}(), 0)
    current = system.children["/"]

    for l in eachline(f)
        # println(l)
        if l[1] == '$'
            if l[3:4] == "cd"
                # println("CD")
                dest = l[6:end]
                if dest == ".."
                    # println("Go up")
                    current = current.parent
                elseif dest == "/"
                    # println("Go root")
                    if current === nothing
                        system.children["/"] = Directory(dest, nothing, Dict(), 0)
                        current = system.children["/"]
                    else
                        current = system.children["/"]
                    end
                    current = system.children["/"]
                else
                    # println("Go down to " * dest)
                    if haskey(current.children, dest)
                        current = current.children[dest]
                    else
                        current.children[dest] = Directory(dest, current, Dict(), 0)
                        current = current.children[dest]
                    end
                end

            elseif l[3:4] == "ls"
                # println("LS")
            end
        else
            if l[1:3] == "dir"
                name = l[5:end]
                # println(("Name of dir", name))
                current.children[name] = Directory(name, current, Dict{String, Any}(), 0)
            else
                size, name = split(l)
                # println((size, name))
                current.children[name] = File(name, parse(Int64, size))
            end
        end
    end

    close(f)

    setsizes(system.children["/"])
    visualize(system.children["/"], 0)

    rootSize = dirSize(system.children["/"])
    spaceAvailable = 70000000 - rootSize
    spaceNeeded = 30000000 - spaceAvailable
    println((rootSize, spaceAvailable, spaceNeeded))

    lst = listsizes(system.children["/"])

    usable::Array{Int64, 1} = filter(x-> x >= spaceNeeded, lst)
    smallest = min(usable...)

    println((lst, usable, smallest))
    smallest
end

# result = work("07/sample.txt")
result = work("07/input.txt")
println("Result: ", result)
# @test result == 95437
