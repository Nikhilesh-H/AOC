# path = r"AOC15\day-07\test.txt"
path = r"AOC15\day-07\input.txt"

with open(path) as f:
    l = f.read().split("\n")

d = {}

while (len(l) != 0):
    
    for instruction in l:
        lhs, rhs = [i.strip() for i in instruction.split("->")]

        try:
            d[rhs] = int(lhs)

        except:
            cmd = lhs.split()

            if len(cmd) == 3:
                if cmd[2] in [str(i) for i in range(100)]:
                    d[cmd[2]] = int(cmd[2])

                if cmd[0] in d and cmd[2] in d:
                    if cmd[1] == "AND":
                        d[rhs] = d[cmd[0]] & d[cmd[2]]
                    elif cmd[1] == "OR":
                        d[rhs] = d[cmd[0]] | d[cmd[2]]
                    elif cmd[1] == "LSHIFT":
                        d[rhs] = d[cmd[0]] << d[cmd[2]]
                    else:
                        d[rhs] = d[cmd[0]] >> d[cmd[2]]

            elif len(cmd) == 2:
                if cmd[1] in [str(i) for i in range(100)]:
                    d[cmd[1]] = int(cmd[1])

                if cmd[1] in d:
                    d[rhs] = 65535 - d[cmd[1]]

            else:
                if cmd[0] in d:
                    d[rhs] = d[cmd[0]]
                    
        if rhs in d:
            l.remove(instruction)

if "a" in d:
    print(d["a"])

else:
    print(d)