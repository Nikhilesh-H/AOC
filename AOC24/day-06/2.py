# path = r"AOC24\day-06\test.txt"
path = r"AOC24\day-06\input.txt"

with open(path) as f:
    grid = f.read().split("\n")
grid = [list(i) for i in grid]

# Finding position of guard in the grid
def find_guard(grid):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] in "^><v":
                return [i, j, grid[i][j]]

# Finding the usual path of the guard
path = set()

temp = [row[:] for row in grid]

guard = find_guard(temp)

while guard[0] not in [0, len(grid)-1] and guard[1] not in [0, len(grid[0])-1]:

    path.add(tuple(guard[:2]))

    temp[guard[0]][guard[1]] = "X"

    if (guard[2]=="^"):
        if temp[guard[0]-1][guard[1]] != "#":
            temp[guard[0]-1][guard[1]] = "^"
            guard[0] -= 1
        else:
            temp[guard[0]][guard[1]] = ">"
            guard[2] = ">"

    elif (guard[2]==">"):
        if temp[guard[0]][guard[1]+1] != "#":
            temp[guard[0]][guard[1]+1] = ">"
            guard[1] += 1
        else:
            temp[guard[0]][guard[1]] = "v"
            guard[2] = "v"

    elif (guard[2]=="<"):
        if temp[guard[0]][guard[1]-1] != "#":
            temp[guard[0]][guard[1]-1] = "<"
            guard[1] -= 1
        else:
            temp[guard[0]][guard[1]] = "^"
            guard[2] = "^"
            
    else:
        if temp[guard[0]+1][guard[1]] != "#":
            temp[guard[0]+1][guard[1]] = "v"
            guard[0] += 1
        else:
            temp[guard[0]][guard[1]] = "<"
            guard[2] = "<"

path.add(tuple(guard[:2]))

result = 0

for (i, j) in path:

    temp = [row[:] for row in grid]

    if temp[i][j] != ".":
        continue

    # Placing an obstacle at each position along the guard's path
    temp[i][j] = "#"

    # To check if the guard enters a loop
    visited = set()

    guard = find_guard(temp)

    while guard[0] not in [0, len(grid)-1] and guard[1] not in [0, len(grid[0])-1]:

        if tuple(guard) in visited:
            result += 1
            break

        visited.add(tuple(guard))

        temp[guard[0]][guard[1]] = "X"

        if (guard[2]=="^"):
            if temp[guard[0]-1][guard[1]] != "#":
                temp[guard[0]-1][guard[1]] = "^"
                guard[0] -= 1
            else:
                temp[guard[0]][guard[1]] = ">"
                guard[2] = ">"

        elif (guard[2]==">"):
            if temp[guard[0]][guard[1]+1] != "#":
                temp[guard[0]][guard[1]+1] = ">"
                guard[1] += 1
            else:
                temp[guard[0]][guard[1]] = "v"
                guard[2] = "v"

        elif (guard[2]=="<"):
            if temp[guard[0]][guard[1]-1] != "#":
                temp[guard[0]][guard[1]-1] = "<"
                guard[1] -= 1
            else:
                temp[guard[0]][guard[1]] = "^"
                guard[2] = "^"
                
        else:
            if temp[guard[0]+1][guard[1]] != "#":
                temp[guard[0]+1][guard[1]] = "v"
                guard[0] += 1
            else:
                temp[guard[0]][guard[1]] = "<"
                guard[2] = "<"

print(result)