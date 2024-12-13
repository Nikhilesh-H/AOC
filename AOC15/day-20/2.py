# path = r"AOC15\day-20\test.txt"
path = r"AOC15\day-20\input.txt"

with open(path) as f:
    target = int(f.read())

gifts = [0]*(int(target/11)+1)

for elf in range(1, int(target/11)+1):
    for house in range(elf, min(int(target/11)+1, elf*51), elf):
        gifts[house] += elf * 11

for gift in range(len(gifts)):
    if gifts[gift] >= target: 
        print(gift)
        break