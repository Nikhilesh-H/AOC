# path = r"AOC24\day-10\test.txt"
path = r"AOC24\day-10\input.txt"

with open(path) as f:
    grid = f.read().split("\n")

grid = [[int(j) for j in list(i)] for i in grid]

zeros = [(i, j) for i in range(len(grid)) for j in range(len(grid)) if grid[i][j] == 0]

def neighbors(index):
    left = grid[index[0]][index[1]-1] if index[1] > 0 else -1
    right = grid[index[0]][index[1]+1] if index[1] < len(grid[0]) - 1 else -1
    up = grid[index[0]-1][index[1]] if index[0] > 0 else -1
    down = grid[index[0]+1][index[1]] if index[0] < len(grid) - 1 else -1
    return left, right, up, down, (index[0], index[1]-1), (index[0], index[1]+1), (index[0]-1, index[1]), (index[0]+1, index[1])

path = set()

def explore(zero, current_pos, current_value, current_path):
    if current_value > 9:
        path.add(tuple([zero] + current_path))
        return
    n = neighbors(current_pos)
    indices = [n[i + 4] for i in range(len(n)-4) if n[i] == current_value]
    for position in indices:
        explore(zero, position, current_value + 1, current_path + [position])

for zero in zeros:
    explore(zero, zero, 1, [])

print(len(path))