# path = r"AOC24\day-14\test.txt"
path = r"AOC24\day-14\input.txt"

with open(path) as f:
    robots = f.read().split("\n")

x, y = (103, 101) if "input" in path else (7, 11)

pos = [i.split()[0] for i in robots]
pos = [i.split("=")[1].split(",") for i in pos]
pos = [[int(i), int(j)] for i, j in pos]
vel = [i.split()[1] for i in robots]
vel = [i.split("=")[1].split(",") for i in vel]
vel = [[int(i), int(j)] for i, j in vel]

for _ in range(101*103):
    grid = [[0]*y for i in range(x)]
    for i in range(len(pos)):
        pos[i][0] = (pos[i][0]+vel[i][0]) % y
        pos[i][1] = (pos[i][1]+vel[i][1]) % x
        grid[pos[i][1]][pos[i][0]] += 1 
    for row in grid:
        if "1111111" in "".join([str(i) for i in row]):
            temp = _+1

print(temp)