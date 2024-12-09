# path = r"AOC24\day-09\test.txt"
path = r"AOC24\day-09\input.txt"

with open(path) as f:
    map = f.read()

compact = []
sizes = {}
id = 0

for i in range(0, len(map)-1, 2):
    compact += [id] * int(map[i]) + [-1] * int(map[i+1])
    sizes[id] = int(map[i])
    id += 1
compact += [id] * int(map[-1])
sizes[id] = int(map[-1])

for fid in sorted(sizes.keys(), reverse = True):
    size = sizes[fid]
    file = compact.index(fid)

    for i in range(file):
        if compact[i:i + size] == [-1] * size:
            compact[i:i+size] = [fid] * size
            compact[file: file+size] = [-1]*size
            break

result = sum([i*compact[i] for i in range(len(compact)) if compact[i] != -1])
print(result)