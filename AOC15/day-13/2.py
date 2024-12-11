# path = r"AOC15\day-13\test.txt"
path = r"AOC15\day-13\input.txt"

with open(path) as f:
    happiness = f.read().split("\n")

n_people = int((1+(1+4*len(happiness))**0.5)/2)

temp = ["x would gain 0"]*n_people
for person in range(len(happiness[::n_people-1])):
    temp += ["x would gain 0"]
    temp.extend(happiness[person*(n_people-1):(person+1)*(n_people-1)])
happiness = temp

n_people = int((1+(1+4*len(happiness))**0.5)/2)

d = {}

for person in range(len(happiness[::n_people-1])):

    l = []

    for line in happiness[person*(n_people-1):(person+1)*(n_people-1)]:
        points = int(line.split()[3])
        if "lose" in line:
            points *= -1
        l.append(points)
        
    l.insert(person, 0)
    d[person+1] = l

from itertools import permutations
perm = permutations([i for i in range(2, n_people+1)])
perm = [[1]+list(i)+[1] for i in perm]

result = 0

for sequence in perm:
    sum = 0
    for i in range(len(sequence)-1):
        sum += d[sequence[i]][sequence[i+1]-1] + d[sequence[i+1]][sequence[i]-1]
    if sum > result:
        result = sum

print(result)