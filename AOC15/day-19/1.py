# path = r"AOC15\day-19\test.txt"
path = r"AOC15\day-19\input.txt"

with open(path) as f:
    rules, compound = f.read().split("\n\n")
rules = rules.split("\n")
rules = [rule.split(" => ") for rule in rules]

possible_molecules = set(rule[0] for rule in rules)
created_molecules = set()

d = {}
for rule in rules:
    if rule[0] not in d: d[rule[0]] = [rule[1]]
    else: d[rule[0]].append(rule[1])

for char in range(len(compound)):

    temp = compound

    if compound[char] in possible_molecules:
        molecule = compound[char]
        a = temp[:char]
        b = temp[char+1:]

    elif compound[char:char + 2] in possible_molecules:
        molecule = compound[char:char+2]
        a = temp[:char]
        b = temp[char+2:]
        char += 1

    else: continue
    
    for i in d[molecule]:
        temp = a + i + b
        created_molecules.add(temp)

print(len(created_molecules))