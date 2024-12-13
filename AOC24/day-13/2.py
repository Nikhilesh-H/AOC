# path = r"AOC24\day-13\test.txt"
path = r"AOC24\day-13\input.txt"

with open(path) as f:
    machines = f.read().split("\n\n")
machines = [machine.split("\n") for machine in machines]

from sympy import symbols, Eq, solve, core

result = 0

for machine in machines:
    A = [int(i.split("+")[-1]) for i in machine[0].split(",")]
    B = [int(i.split("+")[-1]) for i in machine[1].split(",")]
    X = [int(i.split("=")[-1])+10000000000000 for i in machine[2].split(",")]

    i, j = symbols('i,j')
    eq1 = Eq(i*A[0]+j*B[0], X[0]) 
    eq2 = Eq(i*A[1]+j*B[1], X[1]) 
    soln = solve((eq1, eq2), (i, j))
    if "/" not in str(soln[i]) and "/" not in str(soln[j]): result += 3*soln[i] + soln[j]    

print(result)