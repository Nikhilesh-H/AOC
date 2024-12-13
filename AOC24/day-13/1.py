# path = r"AOC24\day-13\test.txt"
path = r"AOC24\day-13\input.txt"

with open(path) as f:
    machines = f.read().split("\n\n")
machines = [machine.split("\n") for machine in machines]

result = 0

for machine in machines:
    A = [int(i.split("+")[-1]) for i in machine[0].split(",")]
    B = [int(i.split("+")[-1]) for i in machine[1].split(",")]
    X = [int(i.split("=")[-1]) for i in machine[2].split(",")]

    for i in range(1, 101):
        for j in range(1, 101):
            cur = [A[0]*i + B[0]*j, A[1]*i + B[1]*j]
            if cur == X: result += i*3 + j
            if cur[0] >= X[0] or cur[1] >= X[1]: break

print(result)