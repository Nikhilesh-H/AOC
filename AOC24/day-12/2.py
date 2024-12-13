# path = r"AOC24\day-12\test.txt"
path = r"AOC24\day-12\input.txt"

with open(path) as f:
    grid = f.read().split("\n")
grid = [list(row) for row in grid]

c = len(grid)*len(grid[0])

def neighbors(index):
    l = []
    value = grid[index[0]][index[1]]
    if index[1] > 0 and grid[index[0]][index[1]-1] == value: l.append([index[0], index[1]-1])
    if index[1] < len(grid[0])-1 and grid[index[0]][index[1]+1] == value: l.append([index[0], index[1]+1] )
    if index[0] > 0 and grid[index[0]-1][index[1]] == value: l.append([index[0]-1, index[1]])
    if index[0] < len(grid) - 1 and grid[index[0]+1][index[1]] == value: l.append([index[0]+1, index[1]])
    return l

def find ():
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] != -1: return [i, j]

region = [[find()]]

while True:
    temp = region[-1][:]

    while (temp):
        neighbor = neighbors(temp.pop(0))
        for i in neighbor:
            if i not in region[-1]:
                temp.append(i)
                region[-1].append(i)

    for i in region[-1]:
        grid[i[0]][i[1]] = -1
        c -= 1

    if c == 0: break

    region.append([find()])

result = 0

for i in region:

    area = len(i)
    sides = 0
    
    corners = []
    for x, y in i:
        corner = [[x, y], [x, y+1], [x+1, y], [x+1, y+1]]
        for j in corner:
            if j not in corners: corners.append(j)

    for corner in corners:
        c = 0
        x, y = corner

        if [x-1, y-1] in i: c+=1
        if [x-1, y] in i: c+=1 
        if [x, y-1] in i: c += 1
        if [x, y] in i: c += 1

        if c in [1, 3]: sides += 1
        elif c==2:
            if ([x-1, y] in i and [x, y-1] in i) or ([x, y] in i and [x-1, y-1] in i): sides += 2

    result += sides * area

print(result)