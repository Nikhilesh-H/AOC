import re

# path = r"AOC24\day-03\test.txt"
path = r"AOC24\day-03\input.txt"

with open(path) as f:
    string = f.read()

# Find instructions which are to be executed
flag = True
new_string = ""
for i in range(len(string)):
    if string[i:i+4] == "do()":
        flag = True
    elif string[i:i+7] == "don't()":
        flag = False
    if (flag):
        new_string += string[i]

# Pattern of instruction
pattern = r"mul\([0-9]+,[0-9]+\)"

result = 0

# Iteratively add all products by finding the patterns
for i in re.findall(pattern, new_string):
    a, b = i[4:-1].split(",")
    result += int(a)*int(b)

print(result)