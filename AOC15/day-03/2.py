# path = r"AOC15\day-03\test.txt"
path = r"AOC15\day-03\input.txt"

with open(path) as f:
    l = f.readlines()

for sequence in l:

    houses = {(0, 0)}
    x, y = 0, 0
    x_robo, y_robo = 0, 0

    for direction in range(len(sequence)):

        if sequence[direction] == "^":
            if direction % 2 == 0:
                y += 1
            else:
                y_robo += 1
        elif sequence[direction] == "v":
            if direction % 2 == 0:
                y -= 1
            else:
                y_robo -= 1
        elif sequence[direction] == ">":
            if direction % 2 == 0:
                x += 1
            else:
                x_robo += 1
        elif sequence[direction] == "<":
            if direction % 2 == 0:
                x -= 1
            else:
                x_robo -= 1
        else:
            continue

        houses.add((x, y))
        houses.add((x_robo, y_robo))

    result = len(houses)
    print(result)