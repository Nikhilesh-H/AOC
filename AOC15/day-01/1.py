# path = r"AOC15\day-01\test.txt"
path = r"AOC15\day-01\input.txt"

with open (path) as f:
    l = f.readlines()

for i in l:
    result = i.count("(") -  i.count(")")
    print(result)