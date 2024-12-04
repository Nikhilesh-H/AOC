# path = r"AOC15\day-03\test.txt"
path = r"AOC15\day-03\input.txt"

with open(path) as f:
    l = f.readlines()

for sequence in l:

    houses = {(0, 0)}
    x, y = 0, 0

    for direction in sequence:

        if direction == "^":
            y += 1
        elif direction == "v":
            y -= 1
        elif direction == ">":
            x += 1
        elif direction == "<":
            x -= 1
        else:
            continue

        houses.add((x, y))

    result = len(houses)
    print(result)