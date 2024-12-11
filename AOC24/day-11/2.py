# path = r"AOC24\day-11\test.txt"
path = r"AOC24\day-11\input.txt"

with open(path) as f:
    stones = [int(i) for i in set(f.read().split())]

d = {i : stones.count(i) for i in stones}
stones = set(stones)

for blink in range(75):
    temp = set()
    temp_d = {}

    for stone in stones:

        new_stones = []

        if stone == 0:
            new_stones.append(1)

        elif len(str(stone)) % 2 == 0:
            new_stones.append(int(str(stone)[:len(str(stone))//2]))
            new_stones.append(int(str(stone)[len(str(stone))//2:]))

        else:
            new_stones.append(stone*2024)

        for new_stone in new_stones:
            if new_stone not in temp:
                temp.add(new_stone)
                temp_d[new_stone] = d[stone]
            else:
                temp_d[new_stone] += d[stone]
                
    stones = temp
    d = temp_d

print(sum(d.values()))