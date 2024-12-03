import re

# path = r"AOC24\day-03\test.txt"
path = r"AOC24\day-03\input.txt"

with open(path) as f:
    string = f.read()

# Pattern of instruction
pattern = r"mul\([0-9]+,[0-9]+\)"

result = 0

# Iteratively add all products by finding the patterns
for i in re.findall(pattern, string):
    a, b = i[4:-1].split(",")
    result += int(a)*int(b)

print(result)