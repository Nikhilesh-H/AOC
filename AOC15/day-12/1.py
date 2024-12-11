# path = r"AOC15\day-12\test.txt"
path = r"AOC15\day-12\input.txt"

with open(path) as f:
    main = f.read()

result = 0

num = ""

for i in main:
    if i.isdigit() or i == "-":
        num += i
    else:
        if num != "":
            result += int(num)
        num = ""

print(result)