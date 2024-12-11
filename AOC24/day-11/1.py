# path = r"AOC24\day-11\test.txt"
path = r"AOC24\day-11\input.txt"

with open(path) as f:
    stones = [int(i) for i in f.read().split()]

for blink in range(25):
    temp = []

    for stone in stones:

        if stone == 0:
            temp.append(1)

        elif len(str(stone)) % 2 == 0:
            temp.append(int(str(stone)[:len(str(stone))//2]))
            temp.append(int(str(stone)[len(str(stone))//2:]))

        else:
            temp.append(stone*2024)

    stones = temp

print(len(stones))