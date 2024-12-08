# path = r"AOC24\day-08\test.txt"
path = r"AOC24\day-08\input.txt"

with open(path) as f:
    grid = f.read()

nodes = set(grid)-{"\n", "."}

grid = grid.split("\n")

antinodes = set()

for node in nodes:

    node_loc = []
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == node:
                node_loc.append([i, j])

    for node_1 in range(len(node_loc)-1):
        for node_2 in range(node_1+1, len(node_loc)):

            pt_1 = node_loc[node_1][:]
            pt_2 = node_loc[node_2][:]
            
            dist = (abs(pt_1[0]-pt_2[0]), abs(pt_1[1]-pt_2[1]))

            antinodes.add(tuple(pt_1))
            antinodes.add(tuple(pt_2))

            while True:

                x = pt_1[0]*2 - pt_2[0]
                y = pt_1[1]*2 - pt_2[1]

                if 0 <= x < len(grid[0]) and 0 <= y < len(grid):
                    antinodes.add((x, y))
                    pt_2 = pt_1[:]
                    pt_1 = [x, y]
                else:
                    break

            while True:

                x = pt_2[0]*2 - pt_1[0]
                y = pt_2[1]*2 - pt_1[1]

                if 0 <= x < len(grid[0]) and 0 <= y < len(grid):
                    antinodes.add((x, y))
                    pt_1 = pt_2[:]
                    pt_2 = [x, y]
                else:
                    break
                
print(len(antinodes))