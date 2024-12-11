path = r"AOC15\day-16\input.txt"

with open(path) as f:
    aunts = f.read().split("\n")

msg = """children: 3
cats: 7
samoyeds: 2
pomeranians: 3
akitas: 0
vizslas: 0
goldfish: 5
trees: 3
cars: 2
perfumes: 1"""

d = {}
for i in msg.split("\n"):
    d[i.split(":")[0]] = int(i.split(":")[1])

for aunt in aunts:

    d_aunt = {}
    l = aunt.split()

    d_aunt[l[2][:-1]] = int(l[3][:-1])
    d_aunt[l[4][:-1]] = int(l[5][:-1])
    d_aunt[l[6][:-1]] = int(l[7])

    flag = True

    for i in d_aunt:
        if d_aunt[i] != d[i]:
            flag = False
            break
        
    if (flag):
        print(l[1][:-1])