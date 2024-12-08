# path = r"AOC24\day-06\test.txt"
path = r"AOC24\day-06\input.txt"

with open(path) as f:
    grid = f.read().split("\n")
grid = [list(i) for i in grid]

# Finding position of guard in the grid
def find_guard():
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] in "^><v":
                return [i, j, grid[i][j]]
            
guard = find_guard()

while guard[0] not in [0, len(grid)-1] and guard[1] not in [0, len(grid[0])-1]:

    grid[guard[0]][guard[1]] = "X"

    if (guard[2]=="^"):
        if grid[guard[0]-1][guard[1]] != "#":
            grid[guard[0]-1][guard[1]] = "^"
            guard[0] -= 1
        else:
            grid[guard[0]][guard[1]] = ">"
            guard[2] = ">"

    elif (guard[2]==">"):
        if grid[guard[0]][guard[1]+1] != "#":
            grid[guard[0]][guard[1]+1] = ">"
            guard[1] += 1
        else:
            grid[guard[0]][guard[1]] = "v"
            guard[2] = "v"

    elif (guard[2]=="<"):
        if grid[guard[0]][guard[1]-1] != "#":
            grid[guard[0]][guard[1]-1] = "<"
            guard[1] -= 1
        else:
            grid[guard[0]][guard[1]] = "^"
            guard[2] = "^"
            
    else:
        if grid[guard[0]+1][guard[1]] != "#":
            grid[guard[0]+1][guard[1]] = "v"
            guard[0] += 1
        else:
            grid[guard[0]][guard[1]] = "<"
            guard[2] = "<"

print(sum([i.count("X") for i in grid]) + 1)