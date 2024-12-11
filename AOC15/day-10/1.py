# path = r"AOC15\day-10\test.txt"
path = r"AOC15\day-10\input.txt"

with open(path) as f:
    sequence = [int(i) for i in f.read()]

for _ in range(40):
    sequence.append(sequence[-1]+1)

    temp = []
    c = 1

    for num in range(len(sequence)-1):
        if sequence[num] == sequence[num+1]:
            c += 1
        else:
            temp.extend([c, sequence[num]])
            c = 1

    sequence = temp

print(len(sequence))