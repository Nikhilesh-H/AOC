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
            
            dist = (abs(node_loc[node_1][0]-node_loc[node_2][0]), abs(node_loc[node_1][1]-node_loc[node_2][1]))
            
            x1 = node_loc[node_1][0]*2 - node_loc[node_2][0]
            y1 = node_loc[node_1][1]*2 - node_loc[node_2][1]
            
            x2 = node_loc[node_2][0]*2 - node_loc[node_1][0]
            y2 = node_loc[node_2][1]*2 - node_loc[node_1][1]

            if 0 <= x1 < len(grid[0]) and 0 <= y1 < len(grid):
                antinodes.add((x1, y1))

            if 0 <= x2 < len(grid[0]) and 0 <= y2 < len(grid):
                antinodes.add((x2, y2))
    
print(len(antinodes))