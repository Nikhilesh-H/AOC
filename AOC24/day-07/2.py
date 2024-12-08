from itertools import permutations

# path = r"AOC24\day-07\test.txt"
path = r"AOC24\day-07\input.txt"

with open(path) as f:
    l = f.read().split("\n")

d = {}

for n in range(2, 13):

    seq = set()

    for i in range(n):
        for j in range(n-i):

            ops = ["add"]*i + ["mul"]*j + ["concat"]*(n-i-j-1)

            perm = permutations(ops) 

            for k in set(perm):
                seq.add(k)

    d[n] = seq

result = 0

for line in l:

    test_value, eqn = line.split(":")

    test_value = int(test_value)
    eqn = [int(i) for i in eqn.split()]
    seq = d[len(eqn)]

    for ops in seq:

        value = eqn[0]

        for op in range(len(ops)):
            if ops[op] == "add":
                value += eqn[op+1]
            elif ops[op] == "mul":
                value *= eqn[op+1]
            else:
                value = int(str(value) + str(eqn[op+1]))
                
        if (test_value == value):
            result += test_value
            break

print(result)