# path = r"AOC24\day-09\test.txt"
path = r"AOC24\day-09\input.txt"

with open(path) as f:
    map = f.read()

compact = []
id = "0"

for i in range(0, len(map)-1, 2):
    compact += [id] * int(map[i]) + ["."] * int(map[i+1])
    id = str(int(id) + 1)
compact += [id] * int(map[-1])

end = len(compact) - 1
for start in range(len(compact) - compact.count(".")):
    if compact[start] == ".":
        while (compact[end] == "."):
            end -= 1
        compact[start], compact[end] = compact[end], compact[start]

result = sum([i * int(compact[i]) for i in range(len(compact)) if compact[i] != "."])
print(result)