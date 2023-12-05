using Test


struct File
    name::String
    size::Int64
end

struct Directory
    name::String
    parent::Any
    children::Dict{String, Any}
end

struct Root
    children::Dict{String, Any}
end

function visualize(children::Dict{String, Any}, level::Int64)

    for (k, v) in children

        if v isa File
            println("  "^level * "- " * v.name)
        elseif v isa Directory
            println("  "^level * "- " * v.name)
            visualize(v.children, level+1)
        end
    end


end

function sumDir(children::Dict{String, Any})
    myLst::Array{Int64, 1} = []
    filesSum = 0
    for (k, v) in children

        if v isa File
            filesSum += v.size
        elseif v isa Directory
            lst = sumDir(v)
            append!(myLst, lst)
        end
    end
    push!(myLst, sum(myLst) + filesSum)
end



function work(filepath::String)
    f = open(filepath)

    # Build tree
    system = Root(Dict{String, Any}())
    system.children["/"] = Directory("/", system, Dict{String, Any}())
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
                        system.children["/"] = Directory(dest, nothing, Dict())
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
                        current.children[dest] = Directory(dest, current, Dict())
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
                current.children[name] = Directory(name, current, Dict{String, Any}())
            else
                size, name = split(l)
                # println((size, name))
                current.children[name] = File(name, parse(Int64, size))
            end
        end
    end

    close(f)

    # println(system)
    visualize(system.children, 0)

    directorySizes = sumDir(system.children)
    println(directorySizes)

    sum(filter(x-> x <= 100000, directorySizes))
end

# result = work("07/sample.txt")
result = work("07/input.txt")
println("Result: ", result)
# @test result == 95437
