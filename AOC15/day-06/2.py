# path = r"AOC15\day-06\test.txt"
path = r"AOC15\day-06\input.txt"

with open(path) as f:
    l = f.readlines()

grid = [[0]*1000 for i in range(1000)]

for instruction in l:
    x1, y1 = [int(i) for i in instruction.split()[-3].split(",")]
    x2, y2 = [int(i) for i in instruction.split()[-1].split(",")]
    
    if " ".join(instruction.split()[:-3]) == "turn on":
        for i in range(x1, x2+1):
            for j in range(y1, y2+1):
                grid[i][j] += 1

    elif " ".join(instruction.split()[:-3]) == "turn off":
        for i in range(x1, x2+1):
            for j in range(y1, y2+1):
                grid[i][j] -= 1 if grid[i][j] > 0 else 0
                
    else:
        for i in range(x1, x2+1):
            for j in range(y1, y2+1):
                grid[i][j] += 2

print(sum([sum(i) for i in grid]))