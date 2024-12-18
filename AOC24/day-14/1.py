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

for _ in range(100):
    for i in range(len(pos)):
        pos[i][0] = (pos[i][0]+vel[i][0]) % y
        pos[i][1] = (pos[i][1]+vel[i][1]) % x

pos = [i for i in pos if i[0] != y//2 and i[1] != x//2]

q1, q2, q3, q4 = [], [], [], []
for i in pos:
    if i[0] < y//2 and i[1] < x//2 : q1. append(i)
    if i[0] < y//2 and i[1] > x//2 : q2. append(i)
    if i[0] > y//2 and i[1] < x//2 : q3. append(i)
    if i[0] > y//2 and i[1] > x//2 : q4. append(i)
print(len(q1)*len(q2)*len(q3)*len(q4))