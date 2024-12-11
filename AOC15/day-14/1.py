# path = r"AOC15\day-14\test.txt"
path = r"AOC15\day-14\input.txt"

with open(path) as f:
    reindeers = f.read().split("\n")

reindeers = [[int(i.split()[3]), int(i.split()[6]), int(i.split()[-2])] for i in reindeers]

race_time = 2503 if "input.txt" in path else 1000

dist = []

for reindeer in reindeers:
    dist.append(reindeer[0] * (reindeer[1]*(race_time//(reindeer[1]+reindeer[2])) + min(reindeer[1], race_time%(reindeer[1]+reindeer[2]))))

print(max(dist))