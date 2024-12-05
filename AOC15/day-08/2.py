# path = r"AOC15\day-08\test.txt"
path = r"AOC15\day-08\input.txt"

with open(path) as f:
    l = f.read().split("\n")

result = 0

for line in l:
    initial = len(line)
    line = line.replace("\\", "\\\\").replace("\"", "\\\"")
    result += len(line) + 2 - initial

print(result)