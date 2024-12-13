# path = r"AOC15\day-19\test.txt"
path = r"AOC15\day-19\input.txt"

with open(path) as f:
    rules, compound = f.read().split("\n\n")
rules = rules.split("\n")
rules = [rule.split(" => ") for rule in rules]

d = {}
for rule in rules:
    d[rule[1]] = rule[0]
    
result = 0

while set(compound) != {"e"}:
    maxi = 0
    molecule = ""
    for i in d:
        if i in compound and len(i) > maxi:
            index = compound.find(i)
            maxi = len(i)
            molecule = i
    compound = compound[:index] + d[molecule] + compound[index+len(molecule):]
    result += 1

print(result)