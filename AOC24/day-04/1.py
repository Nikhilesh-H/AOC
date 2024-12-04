# path = r"AOC24\day-04\test.txt"
path = r"AOC24\day-04\input.txt"

with open(path) as f:
    puzzle = f.read().split("\n")

x = len(puzzle[0])
y = len(puzzle)

# Increase dimension of puzzle from (x, y) to (x+8, y+8) to avoid indexing issues
additional = ["."*(x+8)]*4
puzzle = ["."*4 + i + "."*4 for i in puzzle]
puzzle = additional + puzzle + additional

result = 0

for i in range(4, y+4):
    row = puzzle[i]
    first_top , first_bottom = puzzle[i-1], puzzle[i+1]
    second_top, second_bottom = puzzle[i-2], puzzle[i+2]
    third_top, third_bottom = puzzle[i-3], puzzle[i+3]

    # Check all 8 directions for "XMAS", wherever "X" is found
    for letter in range(4, len(row)-4):
        if row[letter] == "X":
            if row[letter:letter+4] == "XMAS":
                result += 1
            if row[letter:letter-4:-1] == "XMAS":
                result += 1
            if row[letter] + first_bottom[letter] + second_bottom[letter] + third_bottom[letter] == "XMAS":
                result += 1
            if row[letter] + first_top[letter] + second_top[letter] + third_top[letter] == "XMAS":
                result += 1
            if row[letter] + first_top[letter+1] + second_top[letter+2] + third_top[letter+3] == "XMAS":
                result += 1
            if row[letter] + first_top[letter-1] + second_top[letter-2] + third_top[letter-3] == "XMAS":
                result += 1
            if row[letter] + first_bottom[letter-1] + second_bottom[letter-2] + third_bottom[letter-3] == "XMAS":
                result += 1
            if row[letter] + first_bottom[letter+1] + second_bottom[letter+2] + third_bottom[letter+3] == "XMAS":
                result += 1

print(result)