# path = r"AOC24\day-05\test.txt"
path = r"AOC24\day-05\input.txt"

with open(path) as f:
    rules, _, updates = f.read().partition("\n\n")

rules = rules.split("\n")
updates = updates.split("\n")

result = 0

for update in updates:
    sequence = update.split(",")
    flag = 1

    for page in range(len(sequence)-1):
        if sequence[page]+"|"+sequence[page+1] not in rules:
            flag = 0
            break
        
    if (flag):
        result += int(sequence[len(sequence)//2])

print(result)