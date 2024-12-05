from itertools import permutations
import math

# path = r"AOC15\day-09\test.txt"
path = r"AOC15\day-09\input.txt"

with open(path) as f:
    edges = f.read().split("\n")

vertices = set([i.split(" = ")[0].split(" to ")[0] for i in edges])
vertices = vertices.union(set([i.split(" = ")[0].split(" to ")[1] for i in edges]))
vertices = list(vertices)

d = {}
for edge in edges:
    d[edge.split(" = ")[0]] = int(edge.split(" = ")[1])
    d[" ".join(edge.split(" = ")[0].split()[::-1])] = int(edge.split(" = ")[1])

l = permutations(vertices)

result = -math.inf

for i in l:
    cost = 0
    for j in range(len(i)-1):
        cost += d[i[j]+ " to " + i[j+1]]
    if cost > result:
        result = cost

print(result)