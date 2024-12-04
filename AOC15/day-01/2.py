path = r"AOC15\day-01\input.txt"

with open (path) as f:
    string = f.read()

floor = 0

for i in range(len(string)):
    if string[i] == "(":
        floor += 1
    else:
        floor -= 1
        if (floor == -1):
            result = i + 1
            break

print(result)