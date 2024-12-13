# path = r"AOC15\day-18\test.txt"
path = r"AOC15\day-18\input.txt"

with open(path) as f:
    grid = f.read().split()
grid = [list(row) for row in grid]
temp = [row[:] for row in grid]

steps = 4 if "test" in path else 100

for _ in range(steps):
    for i in range(len(grid)):
        for j in range(len(grid[0])):

            neighbors = []
            if i > 0 and j > 0: neighbors.append(grid[i-1][j-1])
            if i > 0: neighbors.append(grid[i-1][j])
            if i > 0 and j < len(grid[0])-1: neighbors.append(grid[i-1][j+1])
            if j > 0: neighbors.append(grid[i][j-1])
            if j < len(grid[0])-1 : neighbors.append(grid[i][j+1])
            if i < len(grid)-1 and j > 0 : neighbors.append(grid[i+1][j-1])
            if i < len(grid)-1: neighbors.append(grid[i+1][j])
            if i < len(grid)-1 and j < len(grid[0]) - 1: neighbors.append(grid[i+1][j+1])

            on = neighbors.count("#")
            if grid[i][j] == "#" and (on < 2 or on > 3) : temp[i][j] = "."
            if grid[i][j] == "." and on == 3: temp[i][j] = "#"

    grid = [row[:] for row in temp]

print("".join(["".join(row) for row in grid]).count("#"))