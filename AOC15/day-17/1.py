from itertools import combinations

# path = r"AOC15\day-17\test.txt"
path = r"AOC15\day-17\input.txt"

with open(path) as f:
    containers = [int(i) for i in f.read().split("\n")]

eggnog = 25 if "test" in path else 150

result = 0

for i in range(1, len(containers)+1):
    possible_comb = combinations(containers, i)
    for comb in possible_comb:
        if sum(comb) == eggnog:
            result += 1

print(result)