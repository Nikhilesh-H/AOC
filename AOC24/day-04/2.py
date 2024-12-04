# path = r"AOC24\day-04\test.txt"
path = r"AOC24\day-04\input.txt"

with open(path) as f:
    puzzle = f.read().split("\n")

x = len(puzzle[0])
y = len(puzzle)

# Increase dimension of puzzle from (x, y) to (x+2, y+2) to avoid indexing issues
additional = ["."*(x+2)]
puzzle = ["." + i + "." for i in puzzle]
puzzle = additional + puzzle + additional

result = 0

for i in range(1, y+1):
    row = puzzle[i]
    first_top , first_bottom = puzzle[i-1], puzzle[i+1]

    # Check both diagonals for "MAS", wherever "A" is found
    for letter in range(1, len(row)-1):
        if row[letter] == "A":
            if (first_top[letter-1] + first_bottom[letter+1] in ["MS", "SM"]) and (first_bottom[letter-1] + first_top[letter+1] in ["MS", "SM"]):
                result += 1

print(result)